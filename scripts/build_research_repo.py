from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


PRODUCTS = [
    ("Hermes Agent", "Hermes Agent", "AI Agents"),
    ("OpenClaw", "OpenClaw", "AI Agents"),
    ("ZeroClaw", "ZeroClaw", "AI Agents"),
    ("TrustClaw", "TrustClaw", "AI Agents"),
    ("Vellum", "Vellum", "AI Development Platforms"),
    ("Manus", "Manus", "AI Agents"),
    ("Lovable", "Lovable", "AI App Builders"),
    ("bolt", "Bolt", "AI App Builders"),
    ("emergent", "Emergent", "AI App Builders"),
    ("Fathom", "Fathom", "Meetings And Transcription"),
    ("Lindy", "Lindy", "AI Agents"),
    ("Canva AI", "Canva AI", "Design And Creative"),
    ("Gamma", "Gamma", "Presentations And Documents"),
    ("NotebookLM", "NotebookLM", "Knowledge And Research"),
    ("Grammarly", "Grammarly", "Writing And Communication"),
    ("Perplexity AI", "Perplexity AI", "Knowledge And Research"),
    ("Jasper AI", "Jasper AI", "Writing And Communication"),
    ("Copy.ai", "Copy.ai", "Writing And Communication"),
    ("Zapier", "Zapier", "Automation And Integration"),
    ("Claude ai", "Claude AI", "AI Assistants"),
    ("Fireflies.ai", "Fireflies.ai", "Meetings And Transcription"),
    ("Notion AI", "Notion AI", "Knowledge And Productivity"),
    ("Reclaim.ai", "Reclaim.ai", "Calendar And Scheduling"),
    ("Kickresume", "Kickresume", "Career And Hiring"),
    ("AIApply", "AIApply", "Career And Hiring"),
    ("Adobe Firefly", "Adobe Firefly", "Media Generation"),
    ("ElevenLabs", "ElevenLabs", "Voice And Audio"),
    ("GitHub Copilot", "GitHub Copilot", "AI Coding"),
    ("Rumway", "Runway", "Media Generation"),
    ("Midjourney", "Midjourney", "Media Generation"),
    ("Google Gemini", "Google Gemini", "AI Assistants"),
    ("HeyGen", "HeyGen", "Media Generation"),
    ("Kling", "Kling", "Media Generation"),
    ("Goblin Tools", "Goblin Tools", "Productivity Tools"),
    ("Fathom", "Fathom", "Meetings And Transcription"),
    ("Lex", "Lex", "Writing And Communication"),
    ("Julius AI", "Julius AI", "Data And Analytics"),
    ("Tableau", "Tableau", "Data And Analytics"),
    ("Figma", "Figma", "Design And Creative"),
    ("Trello", "Trello", "Project Management"),
    ("Otter.ai", "Otter.ai", "Meetings And Transcription"),
    ("Calendly", "Calendly", "Calendar And Scheduling"),
    ("Clockwise", "Clockwise", "Calendar And Scheduling"),
    ("Durable AI", "Durable AI", "AI App Builders"),
    ("Postman", "Postman", "Developer Tools"),
    ("Stack Overflow", "Stack Overflow", "Developer Knowledge"),
    ("Gusto", "Gusto", "Business Operations"),
    ("Ramp", "Ramp", "Finance And Accounting"),
    ("Wave Accounting", "Wave Accounting", "Finance And Accounting"),
    ("ClickUp", "ClickUp", "Project Management"),
    ("Todoist", "Todoist", "Productivity Tools"),
    ("ManyChat", "ManyChat", "Marketing And Sales"),
    ("Buffer", "Buffer", "Marketing And Sales"),
    ("Aider", "Aider", "AI Coding"),
    ("LocalSend", "LocalSend", "Developer Tools"),
    ("Sandbox", "Sandbox", "Ambiguous Products"),
    ("Obsidian", "Obsidian", "Knowledge And Productivity"),
    ("ChatGPT", "ChatGPT", "AI Assistants"),
    ("Google AI Studio", "Google AI Studio", "AI Development Platforms"),
    ("Claude code desktop", "Claude Code Desktop", "AI Coding"),
    ("Claude code CLI", "Claude Code CLI", "AI Coding"),
    ("Claude cowork", "Claude Cowork", "AI Agents"),
    ("Codex CLI", "Codex CLI", "AI Coding"),
    ("Codex desktop", "Codex Desktop", "AI Coding"),
    ("Antigravity CLI", "Antigravity CLI", "AI Coding"),
    ("Antigravity IDE", "Antigravity IDE", "AI Coding"),
    ("Antigravity 2.O", "Antigravity 2.0", "AI Coding"),
    ("Cursor", "Cursor", "AI Coding"),
    ("Perplexity Computer", "Perplexity Computer", "AI Agents"),
    ("wisper flow", "Wispr Flow", "Voice And Audio"),
    ("n8n", "n8n", "Automation And Integration"),
    ("make.com", "Make", "Automation And Integration"),
    ("Humata AI", "Humata AI", "Knowledge And Research"),
    ("Consensus", "Consensus", "Knowledge And Research"),
    ("Elicit", "Elicit", "Knowledge And Research"),
    ("Khroma", "Khroma", "Design And Creative"),
    ("Looka", "Looka", "Design And Creative"),
    ("v0 by Vercel", "v0 by Vercel", "AI App Builders"),
    ("Warp", "Warp", "Developer Tools"),
    ("Browse AI", "Browse AI", "Automation And Integration"),
    ("Clay", "Clay", "Marketing And Sales"),
    ("Flowise", "Flowise", "AI Development Platforms"),
    ("Composio", "Composio", "AI Development Platforms"),
    ("AutoGen", "AutoGen", "AI Development Platforms"),
    ("CrewAI", "CrewAI", "AI Development Platforms"),
    ("Dify", "Dify", "AI Development Platforms"),
    ("Helicone", "Helicone", "AI Development Platforms"),
    ("Greptile", "Greptile", "AI Coding"),
    ("Mintlify", "Mintlify", "Developer Knowledge"),
    ("Unblocked", "Unblocked", "Developer Knowledge"),
    ("Synthetic Users", "Synthetic Users", "UX Research"),
    ("Visily", "Visily", "Design And Creative"),
    ("Relume", "Relume", "Design And Creative"),
    ("Recraft", "Recraft", "Media Generation"),
    ("Meshy", "Meshy", "Media Generation"),
    ("DeepMotion", "DeepMotion", "Media Generation"),
    ("Polycam", "Polycam", "Media Generation"),
    ("Recall", "Recall", "Knowledge And Productivity"),
    ("Jenni AI", "Jenni AI", "Writing And Communication"),
    ("Granola", "Granola", "Meetings And Transcription"),
]


SECTIONS = [
    "Product Overview",
    "Problem It Solves",
    "Core Features",
    "Complete User Journey",
    "Information Architecture",
    "UX Analysis",
    "AI Features",
    "Technical Analysis",
    "Integrations",
    "Automation",
    "Collaboration",
    "Customization",
    "Security",
    "Performance",
    "Community",
    "Strengths",
    "Weaknesses",
    "Missing Features",
    "Hidden Opportunities",
    "Reverse Engineering",
    "Competitive Advantages",
    "Ideal User",
    "SWOT Analysis",
    "Product Rating",
    "Lessons Learned",
]


FEATURE_CATEGORIES = [
    "Core Features",
    "Advanced Features",
    "Hidden Features",
    "Power User Features",
    "Enterprise Features",
    "AI Features",
    "Automation Features",
    "Collaboration Features",
    "Customization Features",
    "Security Features",
    "Developer Features",
    "API Features",
    "Mobile Features",
    "Offline Features",
    "Accessibility Features",
    "Productivity Features",
    "Administration Features",
    "Analytics Features",
    "Billing Features",
    "Notification Features",
    "Search Features",
]


def slug(value):
    value = value.lower().replace("&", "and")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def category_path(category):
    return slug(category)


def report_filename(name):
    return f"{slug(name)}.md"


def template_body(product_name="{Product Name}", original_name="{Original List Label}", category="{Category}"):
    feature_block = "\n".join(
        f"### {name}\n- Description: _To be researched._\n- Why it exists: _To be researched._\n- User benefit: _To be researched._\n"
        for name in FEATURE_CATEGORIES
    )
    sections = {
        "Product Overview": "- Purpose: _To be researched._\n- Primary users: _To be researched._\n- Company: _To be researched._\n- Target market: _To be researched._\n- Pricing model: _To be researched._\n- Business model: _To be researched._\n- Market positioning: _To be researched._\n- Core philosophy: _To be researched._\n- Product vision: _To be researched._",
        "Problem It Solves": "- What problem does it solve? _To be researched._\n- Why does this problem exist? _To be researched._\n- How did people solve this before? _To be researched._\n- Why do users choose this product? _To be researched._",
        "Core Features": feature_block,
        "Complete User Journey": "- Landing page: _To be researched._\n- Signup: _To be researched._\n- Onboarding: _To be researched._\n- First project: _To be researched._\n- Daily usage: _To be researched._\n- Advanced usage: _To be researched._\n- Power user workflow: _To be researched._\n- Long-term retention: _To be researched._\n- Major screens and interactions: _To be researched._",
        "Information Architecture": "- Navigation: _To be researched._\n- Menus: _To be researched._\n- Dashboard: _To be researched._\n- Workspace: _To be researched._\n- Settings: _To be researched._\n- Organization: _To be researched._\n- Hierarchy: _To be researched._\n- Content structure: _To be researched._\n- Folder structure: _To be researched._\n- Projects: _To be researched._\n- Files: _To be researched._\n- Views: _To be researched._",
        "UX Analysis": "- Design philosophy: _To be researched._\n- Interaction model: _To be researched._\n- User experience: _To be researched._\n- Learning curve: _To be researched._\n- Strengths: _To be researched._\n- Weaknesses: _To be researched._\n- Accessibility: _To be researched._\n- Consistency: _To be researched._\n- Visual hierarchy: _To be researched._\n- Navigation quality: _To be researched._",
        "AI Features": "- AI architecture (known/public): _To be researched._\n- Prompt system: _To be researched._\n- Memory: _To be researched._\n- Context: _To be researched._\n- Models: _To be researched._\n- Tools: _To be researched._\n- Agents: _To be researched._\n- Reasoning: _To be researched._\n- Automation: _To be researched._\n- Knowledge: _To be researched._\n- Integrations: _To be researched._\n- Limitations: _To be researched._",
        "Technical Analysis": "- Possible architecture: _To be researched._\n- Frontend: _To be researched._\n- Backend: _To be researched._\n- Infrastructure: _To be researched._\n- Database: _To be researched._\n- Cloud: _To be researched._\n- Caching: _To be researched._\n- Search: _To be researched._\n- Authentication: _To be researched._\n- Storage: _To be researched._\n- Integrations: _To be researched._\n- API: _To be researched._\n- SDK: _To be researched._\n- Extensions: _To be researched._\n- Plugins: _To be researched._\n- Security: _To be researched._\n- Deployment: _To be researched._",
        "Integrations": "- Native: _To be researched._\n- Third-party: _To be researched._\n- API: _To be researched._\n- Zapier: _To be researched._\n- Webhooks: _To be researched._\n- MCP: _To be researched._\n- Browser: _To be researched._\n- Cloud: _To be researched._\n- Communication: _To be researched._\n- Storage: _To be researched._\n- Developer tools: _To be researched._",
        "Automation": "- Triggers: _To be researched._\n- Actions: _To be researched._\n- Scheduling: _To be researched._\n- Agents: _To be researched._\n- Workflows: _To be researched._\n- Logic: _To be researched._\n- Conditions: _To be researched._\n- Approvals: _To be researched._\n- Background tasks: _To be researched._",
        "Collaboration": "- Teams: _To be researched._\n- Sharing: _To be researched._\n- Permissions: _To be researched._\n- Roles: _To be researched._\n- Comments: _To be researched._\n- Presence: _To be researched._\n- Version history: _To be researched._\n- Audit logs: _To be researched._",
        "Customization": "- Themes: _To be researched._\n- Extensions: _To be researched._\n- Templates: _To be researched._\n- Plugins: _To be researched._\n- Widgets: _To be researched._\n- Views: _To be researched._\n- Layouts: _To be researched._\n- Keyboard shortcuts: _To be researched._\n- Settings: _To be researched._",
        "Security": "- Authentication: _To be researched._\n- Authorization: _To be researched._\n- Encryption: _To be researched._\n- Compliance: _To be researched._\n- Permissions: _To be researched._\n- Backup: _To be researched._\n- Recovery: _To be researched._\n- Privacy: _To be researched._",
        "Performance": "- Speed: _To be researched._\n- Scalability: _To be researched._\n- Offline support: _To be researched._\n- Caching: _To be researched._\n- Sync: _To be researched._\n- Reliability: _To be researched._",
        "Community": "- Marketplace: _To be researched._\n- Plugins: _To be researched._\n- Developers: _To be researched._\n- Templates: _To be researched._\n- Forums: _To be researched._\n- GitHub: _To be researched._\n- Discord: _To be researched._\n- Reddit: _To be researched._\n- Learning resources: _To be researched._",
        "Strengths": "- _To be researched._",
        "Weaknesses": "- _To be researched using reviews, forums, GitHub, Reddit, YouTube, Product Hunt, blogs, support pages, feature requests, and issue trackers._",
        "Missing Features": "- Feature: _To be researched._\n- Why it matters: _To be researched._\n- Request frequency: _To be researched._\n- Possible implementation: _To be researched._",
        "Hidden Opportunities": "- Missed opportunities: _To be researched._\n- Unused ideas: _To be researched._\n- Untapped workflows: _To be researched._\n- Future trends: _To be researched._\n- AI opportunities: _To be researched._\n- Automation opportunities: _To be researched._",
        "Reverse Engineering": "- Keep: _To be researched._\n- Redesign: _To be researched._\n- Remove: _To be researched._\n- Simplify: _To be researched._",
        "Competitive Advantages": "- Why users stay: _To be researched._\n- What creates lock-in: _To be researched._\n- Why competitors struggle: _To be researched._",
        "Ideal User": "- Who should use it: _To be researched._\n- Who should avoid it: _To be researched._",
        "SWOT Analysis": "- Strengths: _To be researched._\n- Weaknesses: _To be researched._\n- Opportunities: _To be researched._\n- Threats: _To be researched._",
        "Product Rating": "- Ease of Use: _To be researched._\n- Features: _To be researched._\n- Performance: _To be researched._\n- Customization: _To be researched._\n- AI: _To be researched._\n- Automation: _To be researched._\n- Integrations: _To be researched._\n- Scalability: _To be researched._\n- Innovation: _To be researched._\n- Value for Money: _To be researched._\n- Overall: _To be researched._",
        "Lessons Learned": "- Best ideas worth keeping: _To be researched._\n- Worst ideas to avoid: _To be researched._\n- Innovations worth adapting: _To be researched._\n- Design principles: _To be researched._\n- Architecture principles: _To be researched._\n- Business lessons: _To be researched._\n- Product strategy lessons: _To be researched._",
    }

    lines = [
        f"# {product_name} Research Report",
        "",
        f"- Original list label: {original_name}",
        f"- Normalized product name: {product_name}",
        f"- Category: {category}",
        "- Status: Not started",
        "- Minimum evidence target: 5+ trusted sources where available",
        "",
        "## Source Log",
        "- _Add official docs, changelogs, API docs, public engineering blogs, GitHub repos, reputable reviews, Product Hunt, Reddit/HN/community discussions, and independent reviews._",
        "",
    ]
    for index, section in enumerate(SECTIONS, start=1):
        lines.extend([f"## {index}. {section}", "", sections[section], ""])
    return "\n".join(lines)


def readme(category_rows, total_products):
    return f"""# Product Research ChatGPT

This repository contains independent reverse-engineering research reports for software products and AI tools. The goal is to understand what each product does well, where it fails, and what product, UX, business, architecture, and automation lessons can be reused in a new platform without copying any one product.

## Repository Structure

- `product-registry.md` is the source of truth for product order, normalized names, category placement, and report status.
- `reports/` contains one 25-section Markdown report per product, organized by category folders for easier browsing.
- `combined/complete-product-research-report.md` combines all completed reports in the original list order.
- `discovered-tools/candidates.md` tracks additional relevant products, tools, frameworks, and open-source projects found during research.
- `templates/product-report-template.md` defines the exact 25-section structure every report must follow.

## Progress

- Total unique products after deduplication: {total_products}
- Completed detailed reports: 0
- Current batch: Foundation and report skeletons

## Categories

{category_rows}

## Research Rules

- Keep each product as an independent case study.
- Do not compare products against each other in this phase.
- Use 5+ trusted sources per completed report where available.
- Mark unknowns clearly instead of guessing.
- Keep discovered tools separate until they are approved for full reports.
"""


def combined_report(entries):
    lines = [
        "# Complete Product Research Report",
        "",
        "This master report preserves the original product-list order after deduplicating the repeated Fathom entry. Each detailed report lives in its category folder and will be copied into this file as each batch is completed.",
        "",
        "## Master Order",
        "",
    ]
    for entry in entries:
        lines.append(f"{entry['order']}. [{entry['name']}]({entry['path']}) - {entry['category']} - {entry['status']}")
    lines.extend(["", "## Combined Reports", "", "_Detailed report content will be added here batch by batch._", ""])
    return "\n".join(lines)


def discovered_tools():
    return """# Discovered Tools And Products Candidate List

This file captures additional tools, products, frameworks, APIs, marketplaces, open-source projects, and competitors discovered while researching the main product list.

These candidates are not part of the approved report list yet. They should not receive full reports until approved.

## Candidate Format

| Tool/Product | Category | Why It Appeared | Related Original Product | Source Link | Suggested Reason To Consider |
|---|---|---|---|---|---|
| _To be added during research_ | _To be categorized_ | _Research context_ | _Related product_ | _Source_ | _Why it may matter_ |
"""


def registry(entries):
    lines = [
        "# Product Registry",
        "",
        "This registry preserves the original list order after deduplicating the repeated Fathom entry. Category folders are for browsing only and do not change the research order.",
        "",
        "## Normalization Notes",
        "",
        "- `Fathom` appeared twice and is tracked once.",
        "- `Rumway` is normalized to `Runway` for research accuracy.",
        "- `wisper flow` is normalized to `Wispr Flow` for research accuracy.",
        "- `Antigravity 2.O` is normalized to `Antigravity 2.0`.",
        "- `Sandbox` is kept in Ambiguous Products until research confirms the exact product identity.",
        "",
        "| Order | Original Label | Normalized Name | Category | Report Path | Status |",
        "|---:|---|---|---|---|---|",
    ]
    for entry in entries:
        lines.append(
            f"| {entry['order']} | {entry['original']} | {entry['name']} | {entry['category']} | [{entry['path']}]({entry['path']}) | {entry['status']} |"
        )
    return "\n".join(lines) + "\n"


def main():
    seen = set()
    entries = []
    skipped = []
    for original_index, (original, name, category) in enumerate(PRODUCTS, start=1):
        key = slug(name)
        if key in seen:
            skipped.append((original_index, original, name))
            continue
        seen.add(key)
        path = f"reports/{category_path(category)}/{report_filename(name)}"
        entries.append(
            {
                "order": len(entries) + 1,
                "original_index": original_index,
                "original": original,
                "name": name,
                "category": category,
                "path": path,
                "status": "Not started",
            }
        )

    categories = sorted({entry["category"] for entry in entries})
    category_rows = "\n".join(
        f"- `{category_path(category)}/` - {category}" for category in categories
    )

    files = {
        "README.md": readme(category_rows, len(entries)),
        "product-registry.md": registry(entries),
        "templates/product-report-template.md": template_body(),
        "combined/complete-product-research-report.md": combined_report(entries),
        "discovered-tools/candidates.md": discovered_tools(),
    }

    for entry in entries:
        files[entry["path"]] = template_body(entry["name"], entry["original"], entry["category"])

    for relative_path, content in files.items():
        path = ROOT / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content.rstrip() + "\n", encoding="utf-8")

    gitignore = ROOT / ".gitignore"
    if not gitignore.exists():
        gitignore.write_text(".DS_Store\nThumbs.db\n*.tmp\n.cache/\n", encoding="utf-8")

    print(f"Generated {len(files)} markdown files for {len(entries)} unique products.")
    if skipped:
        for original_index, original, name in skipped:
            print(f"Skipped duplicate at original index {original_index}: {original} -> {name}")


if __name__ == "__main__":
    main()
