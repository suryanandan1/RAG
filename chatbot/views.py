import markdown

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from accounts.models import UserProfile
from .rag import load_rag


qa_chain = load_rag()


@login_required
def chat(request):

    if "chat_history" not in request.session:
        request.session["chat_history"] = []

    chat_history = request.session["chat_history"]

    if request.method == "POST":

        question = request.POST["query"]

        profile, created = UserProfile.objects.get_or_create(
            user=request.user,
            defaults={"band": "9/10"}
        )

        enhanced_query = f"""
Employee Band: {profile.band}

User Question:
{question}

Important Rules:
- Use only the uploaded travel policy documents.
- Employee band is {profile.band}.
- IMPORTANT:
    - 9/10 = senior band
    - 7/8 = mid senior band
    - 5/6 = employee band
    - 1/2/3/4 = junior band
- Answer ONLY for the employee's exact band.
- Never show entitlements of other bands.
- Do not provide details for other bands.
- Give only ONE final answer.
- If the answer is not present in the policy documents, reply exactly:
  This information is not present in the travel policy documents.
- Do not show step-by-step reasoning unless calculation is required.
- Use only the uploaded travel policy documents.
- If the exact city/question is not explicitly mentioned,
  infer the answer strictly from the policy rules and city category.
- Example:
    If user asks about Jaipur travel and Jaipur belongs to Category B,
    answer using Category B rules.
- Only say:
  "This information is not present in the travel policy documents."
  when absolutely no related policy rule exists.
- Use a table only when comparing values or showing calculations.
- If a table is not needed, answer in simple text only.
- Do not use unnecessary headings.
- Do not use HTML tags.

Answer Format Rules:
- If calculation is required, show short calculation steps first, then give the final answer.
- If calculation is required, use a table only when it improves clarity.
- If calculation is not required, answer directly in simple text.
- Do not show unnecessary headings.
- Do not use HTML tags.
"""

        response = qa_chain.invoke(
            {"query": enhanced_query}
        )

        raw_answer = response["result"].replace("**", "").strip()

        if "This information is not present in the travel policy documents." in raw_answer:
            answer = """
            <div class="not-found">
                This information is not present in the travel policy documents.
            </div>
            """
        else:
            answer = markdown.markdown(
                raw_answer,
                extensions=["tables"]
            )

        chat_history.append({
            "question": question,
            "answer": answer
        })

        request.session["chat_history"] = chat_history
        request.session.modified = True

    return render(
        request,
        "chat.html",
        {
            "chat_history": chat_history
        }
    )


def logout_view(request):

    request.session.flush()
    logout(request)

    return redirect("/login/")