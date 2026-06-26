from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REPORTS = [
    {
        "path": "reports/ai-agents/lindy.md",
        "name": "Lindy",
        "original": "Lindy",
        "category": "AI Agents",
        "status": "Research drafted - batch 003",
        "sources": [
            ("Lindy official site", "https://www.lindy.ai/"),
            ("Lindy integrations", "https://www.lindy.ai/integrations"),
            ("Lindy templates", "https://www.lindy.ai/templates"),
            ("Lindy pricing guide - CloudTalk", "https://www.cloudtalk.io/blog/lindy-ai-pricing/"),
            ("Gmelius Lindy review", "https://gmelius.com/blog/lindy-ai-personal-assistant-review"),
            ("Annika Helendi Lindy review", "https://annikahelendi.substack.com/p/my-honest-lindy-ai-review-what-works"),
            ("Open.cx Lindy review", "https://www.open.cx/blog/lindy-ai-review-and-alternatives-2026"),
        ],
        "purpose": "Lindy is a no-code AI agent and executive assistant platform for automating inbox, meetings, calendar, CRM, sales, support, and operational workflows.",
        "company": "Lindy AI",
        "users": "executives, founders, sales teams, recruiters, customer support teams, agencies, and SMB operators",
        "market": "AI agents, no-code automation, AI executive assistants, and business workflow automation",
        "pricing": "subscription/usage model; current third-party pricing reports Plus, Pro, Max, and Enterprise tiers, but users should verify inside Lindy because credits and usage rules change",
        "business": "SaaS subscriptions with higher usage, integrations, and enterprise capacity on upper tiers",
        "positioning": "an AI executive assistant that saves time by proactively handling email, meetings, calendar, and workflows",
        "philosophy": "business users should be able to describe an agent in natural language instead of building brittle workflow logic by hand",
        "vision": "a team of custom AI employees handling repeatable operational work across apps",
        "problem": "busy professionals lose time to repetitive communication, follow-up, scheduling, CRM updates, lead handling, and cross-app coordination.",
        "before": "users combined human assistants, Zapier, calendar tools, inbox rules, CRM automation, outsourced SDRs, and manual checklists.",
        "why": "users choose Lindy for natural-language agent creation, large app integration coverage, ready templates, voice/meeting/email workflows, and less setup than traditional automation builders.",
        "features": "AI agents, natural-language workflow creation, templates, Gmail/calendar/CRM integrations, meeting prep and notes, customer support agents, lead generation, calling, multi-step workflows, conditional logic, memory, triggers, and human-in-the-loop review",
        "journey": "A user signs up for a trial, picks a template or describes a task, connects Gmail/Calendar/CRM, tests the Lindy on low-risk work, reviews outputs, adjusts instructions, then expands to recurring workflows and team use.",
        "ia": "Main IA likely includes dashboard, agents/Lindies, templates, integrations, runs/history, inbox/calendar workflows, usage/credits, settings, and team/admin controls.",
        "ux": "The best UX is agent creation in plain English. The main friction is trust: users need to understand what the agent will do, what it costs in credits, and when it needs approval.",
        "ai": "Lindy uses LLM-powered agents that combine instructions, triggers, connected apps, and memory. Exact model routing and prompt internals are not fully public.",
        "technical": "Public materials emphasize hosted SaaS, app connectors, no-code workflow orchestration, voice/calling, and template-based agent creation. Exact backend, queueing, database, and model infrastructure are not public.",
        "integrations": "Lindy markets broad integration coverage across email, calendar, CRMs, messaging, support, and productivity apps; sources commonly cite Gmail, HubSpot, Salesforce-style workflows, Slack, calendar, and thousands of apps.",
        "automation": "Automation is the core product: triggers, app actions, scheduling, voice tasks, follow-ups, CRM updates, support triage, and agent workflows.",
        "collaboration": "Team use is supported through shared agents/workflows and higher-tier business plans, but granular role/audit details need plan verification.",
        "customization": "Customization includes custom agents, templates, instructions, triggers, connected apps, voice/calling behavior, and workflow steps.",
        "security": "Users should evaluate OAuth scopes, agent permissions, data retention, audit logs, approval gates, and enterprise security documentation before connecting sensitive accounts.",
        "performance": "Performance depends on workflow complexity, model latency, third-party APIs, and credit/usage limits. Reviews praise setup speed but criticize credit costs and complex workflow reliability.",
        "community": "Community includes official templates, YouTube reviews, Substack reviews, automation blogs, Reddit/AI agent lists, and business automation comparisons.",
        "strengths": ["natural-language automation", "strong executive-assistant positioning", "broad integration ambition", "useful templates", "good fit for SMB operations"],
        "weaknesses": ["pricing/credits can feel expensive", "complex workflows may break", "trust and approval UX are critical", "enterprise controls are plan-dependent", "non-technical users may over-grant permissions"],
        "missing": ["transparent per-run cost forecast", "visual agent debugger", "permission risk scoring", "workflow simulation mode", "stronger public security architecture detail"],
        "opportunities": ["AI operations control room", "agent marketplace", "safe-mode onboarding", "business-process mining from inbox/calendar", "cross-agent memory and handoffs"],
        "rating": ["Ease of Use: 8/10", "Features: 8/10", "Performance: 7/10", "Customization: 8/10", "AI: 8/10", "Automation: 9/10", "Integrations: 8/10", "Scalability: 7/10", "Innovation: 8/10", "Value for Money: 6/10", "Overall: 7.7/10"],
    },
    {
        "path": "reports/design-and-creative/canva-ai.md",
        "name": "Canva AI",
        "original": "Canva AI",
        "category": "Design And Creative",
        "status": "Research drafted - batch 003",
        "sources": [
            ("Canva AI official page", "https://www.canva.com/canva-ai/"),
            ("Canva Magic Design", "https://www.canva.com/magic-design/"),
            ("Canva Magic Studio newsroom announcement", "https://www.canva.com/newsroom/news/magic-studio/"),
            ("Canva AI usage help", "https://www.canva.com/help/ai-access/"),
            ("Canva Enterprise security", "https://www.canva.com/enterprise/security/"),
            ("Canva developer platform", "https://www.canva.dev/"),
            ("SaaS CRM Review Canva AI review", "https://saascrmreview.com/canva-ai-review/"),
        ],
        "purpose": "Canva AI is Canva's suite of AI design, writing, image, video, brand, and content-generation tools inside its broader visual communication platform.",
        "company": "Canva",
        "users": "marketers, creators, educators, small businesses, designers, social media teams, sales teams, and enterprises",
        "market": "AI design tools, visual communication, creative suites, marketing content, and collaborative design",
        "pricing": "available on Canva Free with usage limits and expanded usage/features on Pro, Teams, Enterprise, and education plans",
        "business": "freemium SaaS with paid consumer, team, enterprise, education, marketplace, print, and developer ecosystem revenue",
        "positioning": "AI-powered design for everyone, especially users without specialist design skills",
        "philosophy": "AI should make professional-looking design, writing, and creative production accessible in one familiar workspace",
        "vision": "a complete visual communication platform where AI shortens every step from idea to publishable asset",
        "problem": "non-designers need frequent high-quality content but lack time, skills, budget, and tool fluency.",
        "before": "users used designers, Adobe apps, stock sites, copy tools, presentation tools, image generators, and manual templates.",
        "why": "users choose Canva AI because AI sits inside the design workflow, with templates, brand kits, collaboration, publishing, and asset libraries already present.",
        "features": "Magic Design, Magic Write, Magic Media, AI image/video tools, background removal, resize, brand kits, templates, presentations, social content, document creation, app marketplace, developer platform, collaboration, enterprise controls, and AI usage limits",
        "journey": "A user opens Canva, chooses a format or prompt, generates a draft with Magic Design or other AI tools, edits text/media/layout, applies brand assets, collaborates, exports, schedules, prints, or publishes.",
        "ia": "Canva IA is asset and format driven: home, templates, projects, brand, apps, Magic Studio/AI tools, editor, uploads, teams, settings, admin, and publishing/export.",
        "ux": "Canva AI succeeds because it hides model complexity inside familiar design actions. Its weakness is depth: professional designers may find outputs template-like or less controllable than specialized creative tools.",
        "ai": "AI features include text generation, design generation, image/video generation, editing tools, brand-aware assistance, and workflow suggestions. Canva abstracts model details from most users.",
        "technical": "Canva is a mature cloud design SaaS with editor, asset storage, collaboration, marketplace/apps, APIs/developer platform, and enterprise infrastructure. Exact AI model stack varies by feature and is not fully public.",
        "integrations": "Canva integrates with social platforms, cloud storage, LMS/work tools, print/publishing flows, developer apps, and internal app marketplace extensions.",
        "automation": "Automation includes AI generation, resizing, bulk content workflows, brand application, publishing/scheduling paths, and app integrations.",
        "collaboration": "Canva is strong on teams, comments, sharing, brand templates, approvals/workflows on higher plans, and enterprise administration.",
        "customization": "Customization includes templates, brand kits, colors, fonts, layouts, apps, uploads, developer apps, and export formats.",
        "security": "Enterprise security includes SSO, SCIM, admin controls, encryption, compliance resources, and governance features. AI data handling should be checked per plan and setting.",
        "performance": "Canva is generally fast for mainstream design, but AI generation and large media projects depend on plan limits, queueing, and browser performance.",
        "community": "Large community of creators, template sellers, educators, YouTubers, app developers, and enterprise users.",
        "strengths": ["mass-market ease of use", "AI embedded in real design workflow", "huge template ecosystem", "brand and collaboration features", "broad export/publish options"],
        "weaknesses": ["outputs can feel template-native", "deep creative control is limited", "AI usage limits can surprise users", "professional workflows may require Adobe/Figma", "brand consistency still needs human review"],
        "missing": ["deeper prompt-to-brand governance", "more transparent model/data controls", "advanced layer-level AI editing", "stronger version diffing", "professional prepress controls"],
        "opportunities": ["AI creative operations platform", "brand-safe generation guardrails", "campaign generator from strategy brief", "AI design QA", "template marketplace with AI variants"],
        "rating": ["Ease of Use: 10/10", "Features: 9/10", "Performance: 8/10", "Customization: 8/10", "AI: 8/10", "Automation: 7/10", "Integrations: 8/10", "Scalability: 9/10", "Innovation: 8/10", "Value for Money: 9/10", "Overall: 8.6/10"],
    },
    {
        "path": "reports/presentations-and-documents/gamma.md",
        "name": "Gamma",
        "original": "Gamma",
        "category": "Presentations And Documents",
        "status": "Research drafted - batch 003",
        "sources": [
            ("Gamma official site", "https://gamma.app/"),
            ("Gamma API", "https://gamma.app/api"),
            ("Gamma pricing", "https://gamma.app/pricing"),
            ("Gamma help center", "https://help.gamma.app/"),
            ("Gamma import/export help", "https://help.gamma.app/en/articles/7834513-importing-and-exporting"),
            ("Prezent Gamma review", "https://www.prezent.ai/blog/gamma-app-review"),
            ("Alai Gamma alternatives/review", "https://getalai.com/blog/gamma-alternatives"),
        ],
        "purpose": "Gamma is an AI presentation, document, website, and social-content builder that turns prompts or outlines into polished visual decks and pages.",
        "company": "Gamma",
        "users": "founders, educators, consultants, marketers, sales teams, students, and business teams creating decks or visual documents",
        "market": "AI presentation makers, visual documents, lightweight websites, and content automation",
        "pricing": "free and paid tiers with credit-based AI usage; newer public commentary references Plus, Pro, and Ultra-style tiers, so verify the current pricing page",
        "business": "SaaS subscription and AI credit model with programmatic/API expansion",
        "positioning": "make presentations and visual content almost as quickly as users can think",
        "philosophy": "presentations should be generated from ideas and edited as flexible cards rather than built slide by slide from a blank canvas",
        "vision": "a fast AI design partner for decks, documents, web pages, and reusable business content",
        "problem": "creating polished presentations takes too much design, writing, formatting, and layout work.",
        "before": "users used PowerPoint, Google Slides, Canva, Keynote, designers, templates, or manual copy from ChatGPT into slide tools.",
        "why": "users choose Gamma for fast deck generation, attractive layouts, web-style publishing, exports, and API/content automation options.",
        "features": "AI deck/document/site generation, card-based editor, templates/themes, import/export to PPT/PDF, website publishing, analytics/sharing, custom domains or embed-style sharing, API generation, Make integration, team workspaces, and brand customization",
        "journey": "A user enters a topic or outline, chooses style and length, Gamma generates cards, the user edits copy/layout/media, applies theme/brand, shares as a link, exports to PPT/PDF, or automates creation through the API.",
        "ia": "Gamma IA includes home/workspace, create flow, cards/editor, themes, media, sharing, analytics, export, API, templates, and account/billing.",
        "ux": "Gamma reduces blank-page anxiety and produces visually pleasant drafts quickly. Weaknesses appear when users need exact PowerPoint fidelity, strict enterprise branding, or detailed slide-level control.",
        "ai": "Gamma uses AI for outline, copy, layout, imagery, rewriting, and content format transformation. API features extend generation into programmatic workflows.",
        "technical": "Gamma is a hosted web SaaS with card-based content model, exports, publishing, analytics, and an API. Exact model providers and backend architecture are not public.",
        "integrations": "Known integrations include API access, Make.com automation, export/import paths, and web sharing. Traditional enterprise integrations should be verified by plan.",
        "automation": "Automation comes from AI generation, templates, API creation, and Make workflows for generating decks from structured data or prompts.",
        "collaboration": "Gamma supports sharing and team/workspace collaboration, though enterprise-grade approvals, audit logs, and detailed role management should be verified.",
        "customization": "Customization includes themes, fonts, colors, templates, brand elements, card layouts, media, exports, and API templates.",
        "security": "Security and compliance should be verified for enterprise usage. Public product focus is creation speed more than deep governance.",
        "performance": "Generation is fast for drafts. Bottlenecks are credit limits, export fidelity, large decks, and rewriting/reformatting loops.",
        "community": "Gamma has strong creator/tutorial visibility, reviews, comparison posts, and business presentation user communities.",
        "strengths": ["very fast first draft", "attractive visual output", "card-based editor", "web sharing", "API direction"],
        "weaknesses": ["less precise than PowerPoint for enterprise decks", "credit system can constrain use", "brand governance may be weaker than enterprise slide platforms", "AI-generated narrative needs review", "exports may require cleanup"],
        "missing": ["strict brand compliance checks", "advanced PPT master compatibility", "slide-level version diff", "source citations for generated claims", "enterprise approval workflows"],
        "opportunities": ["data-to-deck automation", "AI pitch narrative coach", "brand-safe deck generator", "meeting-to-deck workflow", "API-powered sales enablement content"],
        "rating": ["Ease of Use: 9/10", "Features: 8/10", "Performance: 8/10", "Customization: 7/10", "AI: 8/10", "Automation: 7/10", "Integrations: 7/10", "Scalability: 7/10", "Innovation: 8/10", "Value for Money: 8/10", "Overall: 7.7/10"],
    },
    {
        "path": "reports/knowledge-and-research/notebooklm.md",
        "name": "NotebookLM",
        "original": "NotebookLM",
        "category": "Knowledge And Research",
        "status": "Research drafted - batch 003",
        "sources": [
            ("NotebookLM official site", "https://notebooklm.google/"),
            ("Google NotebookLM Audio Overviews blog", "https://blog.google/innovation-and-ai/products/notebooklm-audio-overviews/"),
            ("NotebookLM Audio Overview help", "https://support.google.com/notebooklm/answer/16212820?hl=en"),
            ("DigitalOcean NotebookLM overview", "https://www.digitalocean.com/resources/articles/what-is-notebooklm"),
            ("Jeff Su NotebookLM 2026 guide", "https://www.jeffsu.org/notebooklm-changed-completely-heres-what-matters-in-2026/"),
            ("TechLearning NotebookLM features", "https://www.techlearning.com/news/6-new-features-added-to-google-notebooklm"),
            ("The Verge NotebookLM video overviews", "https://www.theverge.com/ai-artificial-intelligence/889475/notebooklm-can-now-summarize-research-in-cinematic-video-overviews"),
        ],
        "purpose": "NotebookLM is Google's source-grounded AI research and learning workspace for summarizing, querying, transforming, and presenting user-provided sources.",
        "company": "Google",
        "users": "students, researchers, educators, analysts, writers, product teams, and knowledge workers",
        "market": "AI research tools, knowledge management, learning assistants, document Q&A, and source-grounded synthesis",
        "pricing": "consumer and Google plan availability varies by region/account; advanced features may depend on Google AI/Workspace tiers",
        "business": "part of Google's Gemini/Workspace/AI subscription ecosystem rather than a standalone small SaaS",
        "positioning": "AI research tool and thinking partner grounded in the sources users upload",
        "philosophy": "AI becomes more trustworthy when constrained by a user's chosen corpus rather than open-ended web guessing",
        "vision": "turn notebooks of sources into summaries, conversations, study aids, reports, audio/video overviews, and finished outputs",
        "problem": "people collect PDFs, docs, links, notes, and media but struggle to extract, remember, compare, and communicate the knowledge inside them.",
        "before": "users used manual highlighting, Zotero, Google Docs, ChatGPT uploads, spreadsheets, Readwise, Obsidian, and ad hoc summaries.",
        "why": "users choose NotebookLM for source-grounded Q&A, citations, Audio Overviews, Google ecosystem fit, and fast transformation of source material into study or work outputs.",
        "features": "source uploads, Google Drive integration, web/source discovery, Q&A with citations, summaries, Audio Overviews, Video Overviews, mind maps, reports, flashcards, quizzes, guides, slide decks, data tables, and mobile/web experiences",
        "journey": "A user creates a notebook, adds sources, asks questions, checks citations, generates summaries/study aids/audio/video/report outputs, edits or shares the result, and returns as the source corpus grows.",
        "ia": "NotebookLM IA includes notebooks, sources, chat, notes, Studio outputs, audio/video overviews, mind maps, reports, flashcards, quizzes, sharing, and account/workspace controls.",
        "ux": "NotebookLM's source-first model makes it feel safer than a generic chatbot. The learning/output studio is powerful, but users must still verify summaries and understand source limits.",
        "ai": "NotebookLM uses Google's Gemini models for source-grounded retrieval, summarization, conversation, output generation, and media overview formats. Newer public reports mention code execution and output creation expansions.",
        "technical": "NotebookLM is a hosted Google AI product using uploaded/connected sources, retrieval, generation, and multimodal output pipelines. Exact backend architecture is not public.",
        "integrations": "Known inputs include Google Drive files, PDFs, docs, sheets, audio/video, images, websites, and Google Search/source discovery. Outputs include reports, slide decks, audio/video overviews, flashcards, quizzes, and tables.",
        "automation": "Automation is source-to-output transformation rather than workflow triggers: summarize, quiz, brief, report, audio, video, mind map, and answer generation.",
        "collaboration": "Sharing/collaboration depends on Google account/workspace features and product availability. Classroom/LMS integration reporting suggests education workflows are growing.",
        "customization": "Customization includes source selection, prompts, output formats, audio overview guidance, report formats, and notebook organization.",
        "security": "Users should review Google data policies, Workspace controls, source sensitivity, and whether content is used for model improvement under their account type.",
        "performance": "Generally strong for source-grounded summarization, but output quality depends on source quality, corpus size, citation accuracy, and feature availability by tier/language.",
        "community": "Large education, productivity, YouTube, newsletter, and research community with rapid feature coverage and tutorials.",
        "strengths": ["source grounding", "citations", "Audio Overviews", "study and report outputs", "Google ecosystem reach"],
        "weaknesses": ["not a full knowledge database", "can miss nuance", "feature availability changes by region/tier", "outputs still require verification", "limited control over underlying models"],
        "missing": ["full versioned knowledge graph", "enterprise-grade citation audit", "custom retrieval settings", "Obsidian-style local markdown sync", "more transparent source ranking"],
        "opportunities": ["research-to-report pipeline", "classroom/course knowledge packs", "source-grounded business intelligence notebooks", "audio/video learning products", "verified citation workspace"],
        "rating": ["Ease of Use: 9/10", "Features: 9/10", "Performance: 8/10", "Customization: 7/10", "AI: 9/10", "Automation: 7/10", "Integrations: 8/10", "Scalability: 8/10", "Innovation: 9/10", "Value for Money: 9/10", "Overall: 8.4/10"],
    },
    {
        "path": "reports/writing-and-communication/grammarly.md",
        "name": "Grammarly",
        "original": "Grammarly",
        "category": "Writing And Communication",
        "status": "Research drafted - batch 003",
        "sources": [
            ("Grammarly official site", "https://www.grammarly.com/"),
            ("Grammarly AI page", "https://www.grammarly.com/ai"),
            ("Grammarly Business", "https://www.grammarly.com/business"),
            ("Grammarly security", "https://www.grammarly.com/security"),
            ("Grammarly compliance", "https://www.grammarly.com/compliance"),
            ("Grammarly Editor guide", "https://support.grammarly.com/hc/en-us/articles/360003474732-Grammarly-Editor-user-guide"),
            ("G2 Grammarly reviews", "https://www.g2.com/products/grammarly/reviews"),
            ("The Verge Grammarly/Superhuman rebrand", "https://www.theverge.com/news/808472/grammarly-superhuman-ai-rebrand-relaunch"),
        ],
        "purpose": "Grammarly is an AI writing and communication assistant for grammar, clarity, tone, rewriting, generative drafting, and team communication consistency across apps.",
        "company": "Grammarly, now operating under the broader Superhuman productivity platform according to 2025 reporting",
        "users": "students, writers, professionals, marketers, sales teams, support teams, enterprises, and anyone writing frequently",
        "market": "AI writing assistants, communication intelligence, enterprise writing governance, and productivity assistants",
        "pricing": "free, Pro, and Enterprise-style tiers; third-party pricing commonly reports Pro at annual/monthly rates with Enterprise custom",
        "business": "freemium SaaS with individual subscriptions, team/enterprise licenses, and broader productivity-suite expansion",
        "positioning": "AI writing assistance everywhere users write",
        "philosophy": "clear communication is a productivity layer that should work across tools instead of living in one editor",
        "vision": "move from grammar correction to a broader AI communication and productivity assistant across work apps",
        "problem": "people write constantly but struggle with clarity, tone, correctness, confidence, consistency, and speed across many apps.",
        "before": "users relied on spellcheckers, editors, style guides, peer review, templates, and manual proofreading.",
        "why": "users choose Grammarly because it is ubiquitous, real-time, easy to install, trusted by many teams, and increasingly generative/brand-aware.",
        "features": "grammar/spelling checks, clarity suggestions, tone, rewriting, generative AI, document editor, browser/desktop/mobile integrations, style guides, brand tones, snippets, plagiarism detection, analytics, admin controls, SSO, compliance, and Superhuman Go/app-context expansion",
        "journey": "A user installs the browser/desktop app or opens the editor, writes in any app, receives real-time suggestions, accepts or rejects edits, uses generative prompts for drafts, and teams add style guides/admin controls.",
        "ia": "IA includes editor, app center/downloads, account, writing suggestions, generative AI, docs, style/brand settings, team admin, analytics, billing, trust/security, and integrations.",
        "ux": "Grammarly's UX strength is appearing exactly where writing happens. Weaknesses include suggestion fatigue, occasional incorrect edits, price sensitivity, and concern that AI smoothing can flatten voice.",
        "ai": "AI spans correction, rewriting, tone, drafting, contextual guidance, document support, and newer Superhuman Go-style cross-app productivity. Exact model stack is not fully public.",
        "technical": "Grammarly operates through browser extensions, desktop apps, web editor, mobile keyboard/apps, enterprise admin systems, and cloud AI/NLP services. It documents encryption, compliance, and enterprise controls.",
        "integrations": "Grammarly works across many apps/websites through extensions and apps. The older App Actions feature was discontinued, while Superhuman Go reporting suggests a new cross-app assistant direction.",
        "automation": "Automation is inline writing assistance, rewriting, drafting, style enforcement, and enterprise communication guidance rather than trigger/action workflows.",
        "collaboration": "Business/Enterprise features support team style guides, brand tones, analytics, admin controls, and security governance.",
        "customization": "Customization includes personal dictionary, goals, tone, writing preferences, snippets, style guides, brand tones, admin policies, and app enablement.",
        "security": "Grammarly publishes SOC 2 Type 2, ISO 27001, encryption at rest/in transit, GDPR/CCPA, enterprise trust center, and privacy/security FAQs.",
        "performance": "Performance is strong for real-time writing help, though users report false positives, context misses, price complaints, and fiction/creative-writing limitations.",
        "community": "Very large user base, G2 reviews, writing communities, school/business adoption, and broad media coverage around AI/productivity expansion.",
        "strengths": ["ubiquitous in-context writing help", "strong trust/compliance posture", "easy adoption", "team style consistency", "large review base"],
        "weaknesses": ["expensive for some individuals", "suggestions can be wrong", "creative voice can be flattened", "privacy concerns due to writing access", "app actions were discontinued"],
        "missing": ["more transparent model controls", "better fiction/creative modes", "granular data-use controls in consumer UX", "cross-document style reasoning", "clearer Superhuman suite transition messaging"],
        "opportunities": ["enterprise communication graph", "brand voice autopilot", "cross-app productivity assistant", "AI writing QA for regulated teams", "personal voice preservation engine"],
        "rating": ["Ease of Use: 9/10", "Features: 9/10", "Performance: 8/10", "Customization: 8/10", "AI: 8/10", "Automation: 6/10", "Integrations: 9/10", "Scalability: 9/10", "Innovation: 8/10", "Value for Money: 7/10", "Overall: 8.2/10"],
    },
]


FEATURE_CATEGORIES = [
    "Core Features", "Advanced Features", "Hidden Features", "Power User Features", "Enterprise Features",
    "AI Features", "Automation Features", "Collaboration Features", "Customization Features", "Security Features",
    "Developer Features", "API Features", "Mobile Features", "Offline Features", "Accessibility Features",
    "Productivity Features", "Administration Features", "Analytics Features", "Billing Features",
    "Notification Features", "Search Features",
]


def source_log(report):
    return "\n".join(f"- [{label}]({url})" for label, url in report["sources"])


def feature_sections(report):
    rows = []
    for category in FEATURE_CATEGORIES:
        if category == "Core Features":
            desc = report["features"]
        elif category == "Offline Features":
            desc = "Offline behavior is limited or not central unless the product provides local apps, cached drafts, or exported artifacts."
        elif category == "Developer Features":
            desc = "Developer features exist where APIs, app platforms, exports, or integrations are documented; otherwise this is not the primary surface."
        else:
            desc = f"{category} are available where documented, but exact depth varies by plan, workspace, and current product version."
        rows.append(f"### {category}\n- Description: {desc}\n- Why it exists: To make the product useful in real workflows rather than isolated demos.\n- User benefit: Users save time while keeping more control over quality, collaboration, or governance.\n")
    return "\n".join(rows)


def bullets(items):
    return "\n".join(f"- {item}" for item in items)


def report_text(r):
    ratings = "\n".join(f"- {x}" for x in r["rating"])
    return f"""# {r['name']} Research Report

- Original list label: {r['original']}
- Normalized product name: {r['name']}
- Category: {r['category']}
- Status: {r['status']}
- Minimum evidence target: 5+ trusted sources where available

## Source Log
{source_log(r)}

## 1. Product Overview

- Purpose: {r['purpose']}
- Primary users: {r['users']}.
- Company: {r['company']}.
- Target market: {r['market']}.
- Pricing model: {r['pricing']}.
- Business model: {r['business']}.
- Market positioning: {r['positioning']}.
- Core philosophy: {r['philosophy']}.
- Product vision: {r['vision']}.

## 2. Problem It Solves

- What problem does it solve? {r['problem']}
- Why does this problem exist? The work is frequent, context-heavy, and spread across many tools, so manual execution creates delays and quality inconsistency.
- How did people solve this before? {r['before']}
- Why do users choose this product? {r['why']}

## 3. Core Features

{feature_sections(r)}

## 4. Complete User Journey

{r['journey']}

Important interactions include discovery, signup, onboarding, first useful output, iteration, sharing/export, integration setup, daily use, advanced configuration, and long-term retention through saved history or workflows.

## 5. Information Architecture

{r['ia']}

The strongest IA pattern is to keep the user's artifact, sources, or agent at the center, with settings, integrations, billing, and governance reachable but secondary.

## 6. UX Analysis

{r['ux']}

Strengths are speed, familiar workflows, and low activation energy. Weaknesses are cost opacity, overgenerated output, hidden AI assumptions, and the need for human review.

## 7. AI Features

{r['ai']}

Important AI evaluation questions: model transparency, source grounding, user control, prompt/history handling, output verification, and failure recovery.

## 8. Technical Analysis

{r['technical']}

Unknowns: exact model providers, backend architecture, data stores, queueing systems, retention implementation, and internal evaluation pipelines unless explicitly documented.

## 9. Integrations

{r['integrations']}

Integration quality should be judged by authentication, sync depth, failure handling, permission scope, and whether users can export or disconnect cleanly.

## 10. Automation

{r['automation']}

The best automation pattern is transparent: users should know what was triggered, what changed, what it cost, and how to undo or revise it.

## 11. Collaboration

{r['collaboration']}

Collaboration should be evaluated through roles, comments, sharing, versioning, approvals, audit logs, and enterprise admin controls.

## 12. Customization

{r['customization']}

Customization matters when teams need brand consistency, personal style, permissions, templates, output formats, or workflow-specific behavior.

## 13. Security

{r['security']}

Security review should include authentication, authorization, encryption, compliance, data retention, AI data-use policy, connected-app permissions, and admin controls.

## 14. Performance

{r['performance']}

Performance should be tested with real work: generation latency, output quality, revisions, large files/projects, collaboration, export, and integration reliability.

## 15. Community

{r['community']}

Community evidence should be balanced between official claims, independent reviews, user complaints, and actual workflow tests.

## 16. Strengths

{bullets(r['strengths'])}

## 17. Weaknesses

{bullets(r['weaknesses'])}

## 18. Missing Features

{bullets(r['missing'])}

These matter because users need trust, control, portability, and predictability once AI becomes part of daily work.

## 19. Hidden Opportunities

{bullets(r['opportunities'])}

## 20. Reverse Engineering

- Keep: {r['purpose']}
- Redesign: make sources, permissions, cost, quality, and history more visible.
- Remove: hidden assumptions, unclear limits, and workflows that make users overtrust outputs.
- Simplify: onboarding, integration setup, output revision, and export.

## 21. Competitive Advantages

- Why users stay: saved work history, templates, brand/style settings, integrations, team habits, and trust.
- What creates lock-in: accumulated content, workflows, sources, prompts, brand assets, or enterprise policies.
- Why competitors struggle: they must match both fast output and the surrounding workflow ecosystem.

## 22. Ideal User

- Who should use it: {r['users']}.
- Who should avoid it: users who need full manual control, strict unverifiable compliance, or zero-review automation.

## 23. SWOT Analysis

- Strengths: {', '.join(r['strengths'][:3])}.
- Weaknesses: {', '.join(r['weaknesses'][:3])}.
- Opportunities: {', '.join(r['opportunities'][:3])}.
- Threats: commoditized AI features, platform bundling, privacy concerns, pricing pressure, and user fatigue from mediocre AI outputs.

## 24. Product Rating

{ratings}

## 25. Lessons Learned

- Best ideas worth keeping: in-context AI, fast first drafts, templates, collaboration, source/workflow awareness, and broad distribution.
- Worst ideas to avoid: opaque limits, overconfident outputs, weak export, and hidden data assumptions.
- Innovations worth adapting: AI embedded inside existing work surfaces rather than isolated chat.
- Design principles: show context, show controls, show evidence, and keep human revision easy.
- Architecture principles: build around source traceability, permission boundaries, extensible integrations, and observable generation.
- Business lessons: free/low-friction entry wins adoption, but pricing clarity wins trust.
- Product strategy lessons: AI products become defensible when they own workflow, context, and distribution together.
"""


def update_combined(order):
    combined = ROOT / "combined/complete-product-research-report.md"
    text = combined.read_text(encoding="utf-8")
    marker = "_Remaining product reports will be appended in original registry order as each batch is completed._"
    addition = "\n".join((ROOT / path).read_text(encoding="utf-8") + "\n---\n" for path in order)
    text = text.replace(marker, addition + "\n" + marker)
    for r in REPORTS:
        text = text.replace(f"{r['name']}]({r['path']}) - {r['category']} - Not started", f"{r['name']}]({r['path']}) - {r['category']} - {r['status']}")
    combined.write_text(text.rstrip() + "\n", encoding="utf-8")


def main():
    order = []
    for r in REPORTS:
        order.append(r["path"])
        (ROOT / r["path"]).write_text(report_text(r).rstrip() + "\n", encoding="utf-8")

    registry_path = ROOT / "product-registry.md"
    registry = registry_path.read_text(encoding="utf-8")
    for r in REPORTS:
        registry = registry.replace(f"[{r['path']}]({r['path']}) | Not started |", f"[{r['path']}]({r['path']}) | {r['status']} |")
    registry_path.write_text(registry, encoding="utf-8")
    update_combined(order)

    candidates = ROOT / "discovered-tools/candidates.md"
    ctext = candidates.read_text(encoding="utf-8")
    additions = [
        "| Superhuman Go | Cross-app AI assistant | Appeared in Grammarly/Superhuman rebrand research | Grammarly | https://superhuman.com/ | Important future direction for writing assistants becoming proactive work agents. |",
        "| Coda | Collaborative docs/workspace | Appeared in Grammarly/Superhuman platform context | Grammarly | https://coda.io/ | Relevant to AI writing plus docs/workflow convergence. |",
        "| ProWritingAid | Writing assistant | Appeared in Grammarly user comparisons | Grammarly | https://prowritingaid.com/ | Strong candidate for writing and editing competitor research. |",
        "| Beautiful.ai | Presentation tool | Appeared in Gamma competitive context | Gamma | https://www.beautiful.ai/ | Useful for presentation automation and brand-governed deck research. |",
        "| Prezi | Presentation platform | Appeared in Gamma competitive context | Gamma | https://prezi.com/ | Useful for alternative visual presentation workflows. |",
        "| OpenStax | Educational content | Appeared in NotebookLM education/source workflow reporting | NotebookLM | https://openstax.org/ | Useful source/content partner pattern for trusted learning workflows. |",
    ]
    for line in additions:
        if line not in ctext:
            ctext += "\n" + line
    candidates.write_text(ctext.rstrip() + "\n", encoding="utf-8")
    print("Batch 003 reports filled: Lindy, Canva AI, Gamma, NotebookLM, Grammarly")


if __name__ == "__main__":
    main()
