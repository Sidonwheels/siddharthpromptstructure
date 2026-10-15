# Prompt Engineering Basics: A Beginner's Notebook

A 15-page, notebook-style guide that teaches prompt engineering to complete beginners, with no coding needed.
Built by **Siddharth Bhalla**, Corporate Trainer (Generative AI & Prompt Engineering).

**Live deck:** `https://<your-username>.github.io/prompt-engineering-notebook/`

## What's inside

| Page | Topic |
|------|-------|
| 1 | Cover |
| 2-3 | What a prompt is, and how AI reads it |
| 4-9 | The T C R E I framework: Task, Context, References, Evaluate, Iterate |
| 10 | Full before/after example |
| 11 | Four core techniques: role, few-shot, step by step, format control |
| 12 | One framework across ChatGPT, Claude, and Gemini |
| 13 | Everyday uses: Excel, email, content, learning, summaries |
| 14 | Common mistakes and fixes |
| 15 | 15-minute hands-on exercise and cheat sheet |

The framework is inspired by Google's *Prompting Essentials* course. All wording and examples here are original.

## Files

```
index.html                                 the deck (open in a browser; arrow keys to move)
Prompt_Engineering_Basics_Notebook.pdf     the same 15 pages as a PDF
export_pdf.py                              regenerates the PDF from index.html
.nojekyll                                  lets GitHub Pages serve the files as-is
```

## Publish on GitHub Pages

1. Create a new public repo named `prompt-engineering-notebook` and upload all files.
2. Go to **Settings, Pages**, choose **Deploy from a branch**, select `main` and `/ (root)`, then Save.
3. After about a minute the deck is live at the URL above.

## Regenerate the PDF

```bash
pip install playwright
playwright install chromium
python export_pdf.py
```

## Teaching it live

Each page has a **Try it** box. Pause there, let learners run the prompt in their own AI tool, then compare answers as a group.
