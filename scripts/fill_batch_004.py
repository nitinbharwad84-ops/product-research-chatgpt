from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


FEATURE_CATEGORIES = [
    "Core Features", "Advanced Features", "Hidden Features", "Power User Features", "Enterprise Features",
    "AI Features", "Automation Features", "Collaboration Features", "Customization Features", "Security Features",
    "Developer Features", "API Features", "Mobile Features", "Offline Features", "Accessibility Features",
    "Productivity Features", "Administration Features", "Analytics Features", "Billing Features",
    "Notification Features", "Search Features",
]


REPORTS = [
    {
        "path": "reports/knowledge-and-research/perplexity-ai.md",
        "name": "Perplexity AI",
        "original": "Perplexity AI",
        "category": "Knowledge And Research",
        "status": "Research drafted - batch 004",
        "sources": [
            ("Perplexity official site", "https://www.perplexity.ai/"),
            ("Perplexity Enterprise pricing", "https://www.perplexity.ai/enterprise/pricing"),
            ("Perplexity changelog - API platform", "https://www.perplexity.ai/changelog/what-we-shipped---march-13-2026"),
            ("Perplexity API docs", "https://docs.perplexity.ai/"),
            ("Perplexity Comet", "https://www.perplexity.ai/comet"),
            ("TechJack Perplexity pricing guide", "https://techjacksolutions.com/ai-tools/perplexity/perplexity-pricing/"),
            ("TechRadar Comet browser vulnerability dispute", "https://www.techradar.com/pro/security/perplexity-responds-to-comet-browser-vulnerability-claims-argues-fake-news"),
        ],
        "purpose": "Perplexity AI is an answer engine and research assistant that combines conversational AI with web-grounded search, citations, deep research, enterprise knowledge search, and APIs.",
        "company": "Perplexity AI",
        "users": "students, researchers, executives, analysts, developers, journalists, and teams that need fast source-backed answers",
        "market": "AI search, answer engines, research assistants, enterprise knowledge search, and web-grounded AI APIs",
        "pricing": "free, Pro, Max/advanced consumer tiers, Enterprise Pro, and API usage; official enterprise pricing should be checked because public summaries change often",
        "business": "consumer subscriptions, enterprise seats, advertising/commerce experiments, browser distribution, and API usage",
        "positioning": "a faster answer engine for people who want sourced answers instead of a page of links",
        "philosophy": "AI search should answer directly while exposing sources so users can verify claims",
        "vision": "replace parts of traditional search, research, and knowledge work with trustworthy AI answers and agentic browsing",
        "problem": "traditional search requires opening many tabs, judging sources manually, and synthesizing results; generic chatbots can answer without enough evidence.",
        "before": "users searched Google/Bing, read articles manually, used ChatGPT with browsing, used research assistants, or maintained internal knowledge bases.",
        "why": "users choose it for citations, fast web-grounded answers, Deep Research, model choice, file/internal search, Comet browser, and developer APIs.",
        "features": "web answers with citations, Pro Search, Deep Research, Pages, Spaces/collections, file upload, model selection, image generation, Comet browser, enterprise internal knowledge search, Agent/Search/Embeddings APIs, and mobile/browser apps",
        "journey": "A user asks a question, reviews the cited answer, opens sources, follows up conversationally, saves or shares results, uses Deep Research for larger topics, uploads files or uses enterprise knowledge, and may use Comet or APIs for deeper workflows.",
        "ia": "IA includes home/search, answer thread, sources, follow-ups, library/history, Spaces, Discover, files, settings, model controls, enterprise/admin, API docs, and Comet/browser surfaces.",
        "ux": "The UX is strongest when a user needs quick research with visible citations. Weaknesses include occasional source mismatch, overconfident synthesis, SEO/content-farm exposure, and the need to verify anything high stakes.",
        "ai": "AI features include RAG-style search grounding, multiple models, deep research, internal knowledge retrieval, agent APIs, search APIs, embeddings APIs, and browser-agent ambitions.",
        "technical": "Public docs position Perplexity API as model-agnostic infrastructure for agents with search, agent orchestration, embeddings, and upcoming sandbox execution. Exact ranking/retrieval/model routing internals are not fully public.",
        "integrations": "Key surfaces include browser/mobile apps, Comet, API, enterprise internal files/knowledge, citation links, and possible workflow integrations through API users.",
        "automation": "Automation is moving from search to agent workflows through API platform, Comet, and deep research. Users still need human verification for important outputs.",
        "collaboration": "Enterprise offerings add team knowledge/search and admin features. Public personal collaboration is more lightweight through sharing, Pages, Spaces, and links.",
        "customization": "Customization includes model choice, search mode, Spaces, uploaded/internal sources, enterprise controls, and API parameters.",
        "security": "Enterprise plans emphasize team privacy and internal knowledge controls. Comet/browser-agent security disputes show that agentic browsing needs careful sandboxing and consent design.",
        "performance": "Very strong for quick research, but quality depends on source availability, retrieval freshness, citation quality, model choice, and task complexity.",
        "community": "Large user base, active social/media discussion, enterprise coverage, API developers, SEO/search debates, and browser security commentary.",
        "strengths": ["fast cited answers", "strong research UX", "deep research capability", "enterprise knowledge direction", "API platform expansion"],
        "weaknesses": ["citations still require checking", "pricing and plan limits can be confusing", "browser-agent security concerns", "source quality varies", "less controllable than a dedicated research workflow"],
        "missing": ["source-quality scoring", "citation audit trail", "enterprise evaluation dashboards", "better false-source warnings", "transparent retrieval/ranking controls"],
        "opportunities": ["verified research workspace", "enterprise search plus workflow automation", "agent-safe browser patterns", "research-to-report pipelines", "API layer for trustworthy AI apps"],
        "rating": ["Ease of Use: 9/10", "Features: 9/10", "Performance: 8/10", "Customization: 7/10", "AI: 9/10", "Automation: 7/10", "Integrations: 8/10", "Scalability: 8/10", "Innovation: 9/10", "Value for Money: 8/10", "Overall: 8.3/10"],
    },
    {
        "path": "reports/writing-and-communication/jasper-ai.md",
        "name": "Jasper AI",
        "original": "Jasper AI",
        "category": "Writing And Communication",
        "status": "Research drafted - batch 004",
        "sources": [
            ("Jasper official site", "https://www.jasper.ai/"),
            ("Jasper pricing", "https://www.jasper.ai/pricing"),
            ("Jasper brand voice", "https://www.jasper.ai/features/brand-voice"),
            ("Jasper AI agents", "https://www.jasper.ai/features/ai-agents"),
            ("Jasper trust center", "https://www.jasper.ai/trust-center"),
            ("PikaSEO Jasper review", "https://pikaseo.com/articles/jasper-ai-review"),
            ("SaaS CRM Review Jasper pricing", "https://saascrmreview.com/jasper-ai-pricing/"),
            ("Fritz AI Jasper review", "https://fritz.ai/jasper-ai-review/"),
        ],
        "purpose": "Jasper AI is a marketing-focused AI platform for creating brand-consistent content, campaigns, copy, images, and marketing workflows.",
        "company": "Jasper",
        "users": "marketing teams, agencies, content teams, enterprise brands, campaign managers, and revenue teams",
        "market": "AI marketing platforms, enterprise content generation, brand voice, and campaign automation",
        "pricing": "Pro plan and custom Business plan with trial options; public guides commonly frame Jasper as premium-priced compared with casual AI writers",
        "business": "SaaS subscriptions and enterprise contracts for marketing teams",
        "positioning": "AI purpose-built for marketing, not a generic chatbot",
        "philosophy": "marketing AI must preserve brand voice, campaign context, and workflow repeatability",
        "vision": "a marketing AI system that helps teams produce high-quality, on-brand campaigns at scale",
        "problem": "marketing teams need more content across more channels while preserving voice, strategy, approvals, and performance.",
        "before": "teams used freelancers, agencies, ChatGPT, spreadsheets, CMS drafts, SEO tools, design tools, and manual brand guidelines.",
        "why": "users choose Jasper for brand voice, marketing templates, campaign workflows, AI agents, collaboration, and enterprise security.",
        "features": "brand voice, knowledge assets, campaign generation, marketing templates, AI agents, chat, image generation, SEO/content workflows, team collaboration, governance, browser extension, and enterprise security",
        "journey": "A marketer creates a workspace, adds brand voice and company knowledge, picks a campaign or template, generates drafts, collaborates with teammates, edits for strategy/accuracy, and publishes through the team's normal channels.",
        "ia": "IA includes dashboard, campaigns, brand voice, knowledge, templates, agents, chat/editor, assets, team settings, billing, and trust/admin areas.",
        "ux": "Jasper's UX is good for marketers because it packages AI around campaign jobs. Its weakness is cost and complexity for users who only need occasional writing.",
        "ai": "Jasper uses AI agents, brand voice models/settings, marketing templates, chat, image generation, and workflow-specific generation. Exact model routing is abstracted.",
        "technical": "Jasper is hosted SaaS with brand/knowledge storage, generation workflows, team controls, and integrations. Exact backend/model architecture is not public.",
        "integrations": "Public surfaces include browser extension and marketing workflow integrations; SEO and content ecosystem integrations should be verified against current plan docs.",
        "automation": "Automation includes campaign generation, template-driven content workflows, brand voice application, agent tasks, and repeatable marketing production flows.",
        "collaboration": "Designed for teams with shared brand assets, campaign workspaces, collaboration, admin, and enterprise governance.",
        "customization": "Strong customization around brand voice, audiences, tone, templates, knowledge, campaigns, and workflows.",
        "security": "Trust center and enterprise positioning emphasize security, governance, and business-grade controls; users should verify SSO, data handling, and retention by plan.",
        "performance": "Strong for structured marketing output. Weaknesses appear when outputs need deep originality, precise strategy, or cost-effective casual use.",
        "community": "Mature review ecosystem, marketing blog coverage, tutorials, agency discussions, and alternatives comparisons.",
        "strengths": ["brand voice focus", "marketing-specific workflows", "enterprise positioning", "campaign scale", "good for agencies/teams"],
        "weaknesses": ["premium price", "less compelling for casual writers", "output still needs editing", "brand voice can become formulaic", "not a full marketing operations suite"],
        "missing": ["stronger performance attribution", "native approval workflow depth", "transparent model controls", "campaign ROI loop", "better small-team pricing"],
        "opportunities": ["AI campaign operating system", "brand-compliance scoring", "marketing memory graph", "automated content testing", "creative strategy copilot"],
        "rating": ["Ease of Use: 8/10", "Features: 8/10", "Performance: 8/10", "Customization: 9/10", "AI: 8/10", "Automation: 7/10", "Integrations: 7/10", "Scalability: 8/10", "Innovation: 7/10", "Value for Money: 6/10", "Overall: 7.6/10"],
    },
    {
        "path": "reports/writing-and-communication/copy-ai.md",
        "name": "Copy.ai",
        "original": "Copy.ai",
        "category": "Writing And Communication",
        "status": "Research drafted - batch 004",
        "sources": [
            ("Copy.ai official site", "https://www.copy.ai/"),
            ("Copy.ai platform overview blog", "https://www.copy.ai/blog/copyai"),
            ("Copy.ai workflows", "https://www.copy.ai/workflows"),
            ("Copy.ai free trial", "https://www.copy.ai/blog/copy-ai-free-trial"),
            ("Copy.ai pricing", "https://www.copy.ai/prices"),
            ("SalesRobot Copy.ai review", "https://www.salesrobot.co/blogs/copyai-review"),
            ("Jingrey Copy.ai review", "https://jingrey.com/tools/copyai/"),
        ],
        "purpose": "Copy.ai is a GTM AI platform for automating sales and marketing workflows, content creation, prospecting, enrichment, and revenue-team processes.",
        "company": "Copy.ai",
        "users": "sales teams, marketing teams, growth teams, agencies, revenue operations, and GTM leaders",
        "market": "GTM AI, sales/marketing automation, AI copywriting, revenue workflow orchestration",
        "pricing": "free trial and paid plans; current pricing should be verified because Copy.ai has shifted from copywriting toward GTM workflow platform packaging",
        "business": "SaaS subscription for GTM teams and enterprise workflow automation",
        "positioning": "GTM AI platform rather than only an AI copywriting tool",
        "philosophy": "AI should orchestrate revenue workflows across data, apps, and teams instead of generating isolated copy snippets",
        "vision": "an AI operating layer for go-to-market teams",
        "problem": "sales and marketing teams have fragmented data, repetitive research, manual personalization, CRM updates, and disconnected content workflows.",
        "before": "teams used SDR tools, enrichment tools, CRM tasks, spreadsheets, ChatGPT, Jasper, Zapier, agencies, and manual copy workflows.",
        "why": "users choose Copy.ai for GTM workflows, sales/marketing templates, copy generation, brand voice, Infobase, agents, and workflow orchestration.",
        "features": "GTM workflows, Copy Agents, Infobase, brand voice, tables, actions, chat, sales prospecting, content generation, CRM-style workflow automation, multi-model routing, and team collaboration",
        "journey": "A team maps a GTM process, loads company knowledge, creates or selects a workflow, connects data/apps, runs enrichment or content steps, reviews outputs, and syncs results into sales/marketing systems.",
        "ia": "IA includes platform overview, workflows, agents, Infobase, tables, actions, brand voice, chat, use cases, integrations, billing, and admin.",
        "ux": "Copy.ai's newer GTM positioning is stronger for revenue teams than casual writers. The UX challenge is explaining workflow orchestration without overwhelming users who came for simple copy generation.",
        "ai": "AI is used for multi-step GTM workflows, copy generation, personalization, research, enrichment, and agent-like process automation. Model routing is largely abstracted.",
        "technical": "Hosted SaaS with workflow orchestration, knowledge layer, tables/actions, AI generation, and integrations. Exact backend stack is not public.",
        "integrations": "The platform connects with GTM systems and CRM/data workflows; exact native integrations should be verified from the current app and docs.",
        "automation": "Automation is central: lead research, email/personalization, enrichment, CRM updates, content workflows, and GTM process execution.",
        "collaboration": "Team workflows, shared knowledge, and GTM process templates support collaboration, though enterprise governance depth needs verification by plan.",
        "customization": "Customization includes workflows, agents, brand voice, Infobase, tables, actions, prompts, and GTM use cases.",
        "security": "Security posture should be evaluated for CRM/customer data, AI data use, permissions, audit logs, and enterprise controls.",
        "performance": "Good fit for repeatable GTM processes; less ideal for nuanced long-form content or teams without a clearly defined process.",
        "community": "Reviews, sales-tech comparisons, YouTube demos, GTM blogs, and AI copywriting community history.",
        "strengths": ["clear GTM specialization", "workflow orientation", "brand/knowledge layer", "sales and marketing templates", "stronger than generic chat for repeatable processes"],
        "weaknesses": ["less simple than older copywriting positioning", "requires process clarity", "long-form quality still needs editing", "integration depth must be verified", "pricing/packaging can be unclear"],
        "missing": ["native ROI analytics", "clear integration matrix", "workflow debugger", "governance/audit detail", "better migration from old copywriter use case"],
        "opportunities": ["GTM process automation hub", "AI SDR workflow library", "revenue knowledge graph", "workflow QA/testing", "CRM-safe agent approvals"],
        "rating": ["Ease of Use: 7/10", "Features: 8/10", "Performance: 7/10", "Customization: 8/10", "AI: 8/10", "Automation: 8/10", "Integrations: 7/10", "Scalability: 8/10", "Innovation: 8/10", "Value for Money: 7/10", "Overall: 7.6/10"],
    },
    {
        "path": "reports/automation-and-integration/zapier.md",
        "name": "Zapier",
        "original": "Zapier",
        "category": "Automation And Integration",
        "status": "Research drafted - batch 004",
        "sources": [
            ("Zapier official site", "https://zapier.com/"),
            ("Zapier pricing", "https://zapier.com/pricing"),
            ("Zapier integrations", "https://zapier.com/apps"),
            ("Zapier AI agents guide", "https://zapier.com/blog/best-ai-agents/"),
            ("Zapier MCP", "https://zapier.com/mcp"),
            ("Zapier developer platform", "https://platform.zapier.com/"),
            ("Arahi AI Zapier vs agents comparison", "https://arahi.ai/blog/ai-agent-vs-zapier-automation-comparison-2025"),
            ("TechRadar AI tools Zapier coverage", "https://www.techradar.com/best/best-ai-tools"),
        ],
        "purpose": "Zapier is a no-code automation platform connecting thousands of apps with triggers, actions, multi-step workflows, AI-powered builders, agents, MCP, and developer extensibility.",
        "company": "Zapier",
        "users": "non-technical teams, operations teams, marketers, sales teams, support teams, founders, agencies, and developers building integrations",
        "market": "workflow automation, iPaaS, no-code integration, AI automation, and app connectivity",
        "pricing": "free and paid plans with task/usage limits; paid plans commonly start around the low-$20/month range when billed annually, but current pricing should be checked",
        "business": "subscription and usage-based SaaS with team, company, and enterprise tiers",
        "positioning": "connect your apps and automate work without code",
        "philosophy": "business users should be able to automate cross-app work without waiting for engineering",
        "vision": "a universal automation layer for business apps, now expanded with AI builders and agents",
        "problem": "business processes span many SaaS tools, causing repetitive copy/paste, missed handoffs, and fragile manual coordination.",
        "before": "teams wrote custom scripts, used spreadsheets, hired ops specialists, relied on app-native integrations, or manually moved data between tools.",
        "why": "users choose Zapier for massive integration coverage, templates, predictable trigger/action automation, AI-assisted workflow creation, and broad ecosystem trust.",
        "features": "Zaps, triggers, actions, filters, paths, schedules, tables, interfaces, webhooks, app integrations, AI actions, AI agents, Copilot-style builders, MCP, developer platform, team/admin controls, and task history",
        "journey": "A user chooses a template or describes an automation, connects apps, maps fields, tests a trigger/action, turns on the Zap, monitors runs, debugs failed tasks, and expands into multi-step workflows or AI agents.",
        "ia": "IA includes dashboard, Zaps, templates, apps, task history, tables, interfaces, agents, MCP, billing/tasks, connected accounts, team/admin, and developer platform.",
        "ux": "Zapier is approachable for simple automations and powerful for ops teams. Complexity rises with multi-step logic, task costs, error handling, and AI-agent behavior.",
        "ai": "AI appears in workflow building, AI actions, agents, app-connected AI workflows, and MCP so AI assistants can take actions across Zapier-connected apps.",
        "technical": "Zapier is a mature hosted automation platform with trigger polling/webhooks, app connectors, task execution, developer platform, logs, credentials, and governance controls. Exact internals are not public.",
        "integrations": "Zapier markets thousands of app integrations, webhooks, developer-built apps, MCP, and AI-agent action surfaces.",
        "automation": "Automation is Zapier's core: triggers, actions, paths, filters, delays, schedules, webhooks, AI actions, agents, and reusable templates.",
        "collaboration": "Team/company plans support shared workflows, connected accounts, folders, admin, governance, and enterprise controls.",
        "customization": "Customization includes multi-step logic, custom webhooks, code steps, developer platform apps, tables/interfaces, and AI instructions.",
        "security": "Enterprise controls include app/account governance, admin settings, SSO-style features on higher tiers, logs, and credential management; users must still scope connected accounts carefully.",
        "performance": "Reliable for broad business automation, but polling intervals, task limits, error retries, and app API limits affect time-sensitive workflows.",
        "community": "Huge ecosystem of templates, experts, freelancers, developers, YouTube tutorials, agencies, and app partners.",
        "strengths": ["massive integration library", "mature automation patterns", "non-technical accessibility", "templates and ecosystem", "AI/MCP expansion"],
        "weaknesses": ["task pricing can scale quickly", "complex workflows get hard to debug", "polling delays limit real-time use", "AI agents add unpredictability", "some app connectors are shallow"],
        "missing": ["clearer cost simulation", "visual run replay", "stronger mobile management", "native process mining", "AI action risk scoring"],
        "opportunities": ["AI automation governance", "MCP action marketplace", "ops observability layer", "workflow cost optimizer", "human approval inbox for AI agents"],
        "rating": ["Ease of Use: 8/10", "Features: 10/10", "Performance: 8/10", "Customization: 9/10", "AI: 8/10", "Automation: 10/10", "Integrations: 10/10", "Scalability: 9/10", "Innovation: 8/10", "Value for Money: 7/10", "Overall: 8.8/10"],
    },
    {
        "path": "reports/ai-assistants/claude-ai.md",
        "name": "Claude AI",
        "original": "Claude ai",
        "category": "AI Assistants",
        "status": "Research drafted - batch 004",
        "sources": [
            ("Anthropic official site", "https://www.anthropic.com/"),
            ("Claude official app", "https://claude.ai/"),
            ("Claude platform docs", "https://platform.claude.com/docs"),
            ("Claude platform pricing", "https://platform.claude.com/docs/en/about-claude/pricing"),
            ("Claude Artifacts help", "https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them"),
            ("Anthropic Projects announcement", "https://www.anthropic.com/news/projects"),
            ("Anthropic Trust Center", "https://trust.anthropic.com/"),
            ("Anthropic certification article", "https://privacy.claude.com/en/articles/10015870-what-certifications-has-anthropic-obtained"),
            ("G2 Claude reviews", "https://www.g2.com/products/claude-2025-12-11/reviews"),
        ],
        "purpose": "Claude AI is Anthropic's conversational AI assistant and model platform for writing, analysis, coding, reasoning, artifacts, projects, enterprise work, and API-based development.",
        "company": "Anthropic",
        "users": "individual knowledge workers, developers, students, analysts, writers, enterprises, product teams, and AI builders",
        "market": "general AI assistants, frontier models, enterprise AI, developer APIs, and AI coding/agent tools",
        "pricing": "Free, Pro, Max, Team/Enterprise, and API pricing; API costs depend on model, input/output tokens, caching, and batch usage",
        "business": "consumer subscriptions, team/enterprise seats, API usage, cloud partnerships, and platform integrations",
        "positioning": "a reliable, thoughtful, safety-focused AI assistant for serious work",
        "philosophy": "frontier AI should be helpful, harmless, honest, steerable, and enterprise-ready",
        "vision": "build reliable, interpretable, and steerable AI systems that can assist people and organizations safely",
        "problem": "users need high-quality reasoning, writing, coding, and analysis, but generic AI can be unsafe, ungrounded, hard to steer, or weak in long-context work.",
        "before": "users used search engines, ChatGPT, manual analysis, writing tools, coding assistants, consultants, or separate API/model providers.",
        "why": "users choose Claude for strong writing, reasoning, long context, Artifacts, Projects, coding support, API quality, trust posture, and enterprise security.",
        "features": "chat, long context, Artifacts, Projects, file upload, analysis, coding, Claude Code, API/models, tool use, MCP ecosystem, Team/Enterprise controls, mobile/desktop/web apps, and trust/compliance resources",
        "journey": "A user signs up, asks a task, uploads files or creates a project, iterates in chat, uses Artifacts for substantial outputs, saves context in Projects, then expands to team/API/Claude Code workflows.",
        "ia": "IA includes chats, projects, artifacts, files, settings, plan/usage, model controls, organization/admin, API console/docs, trust center, and developer resources.",
        "ux": "Claude feels calm and strong for writing, reasoning, and structured work. Friction appears around usage caps, plan jumps, feature availability, and lack of visible internals for memory/context decisions.",
        "ai": "Claude includes frontier language models, reasoning modes, long context, tool use, artifacts, projects, coding agents, API features, and safety alignment work. Exact training data and prompt internals are not public.",
        "technical": "Anthropic provides hosted Claude apps and API models through its platform and cloud partners. Public docs cover API usage, pricing, tool use, model behavior, and compliance; internal infrastructure is not fully public.",
        "integrations": "Claude integrates through API, cloud platforms, MCP ecosystem, Claude Code, enterprise deployments, and app surfaces. Third-party integrations include many tools built around Anthropic models.",
        "automation": "Automation appears through API tool use, Claude Code, scheduled/agentic features in adjacent Claude products, and workflows built by developers. Claude chat itself remains human-in-the-loop.",
        "collaboration": "Projects and Team/Enterprise plans support shared context and organizational usage; exact collaboration and admin depth depend on plan.",
        "customization": "Customization includes project instructions, style, uploaded context, tool/API usage, model choice, system prompts in API, and enterprise controls.",
        "security": "Anthropic publishes trust resources, certifications, HIPAA-ready configuration for commercial products, ISO 27001, and security/privacy documentation. Users should verify plan-specific data training and retention settings.",
        "performance": "Claude is highly regarded for writing, reasoning, coding, and long-context analysis. Weak spots include usage caps, occasional refusals, hallucinations, and cost for heavy API workloads.",
        "community": "Large community across ClaudeAI Reddit, developer forums, G2, YouTube, enterprise AI reports, coding communities, and Anthropic research followers.",
        "strengths": ["high-quality writing and reasoning", "Artifacts are excellent for substantial outputs", "strong developer/API ecosystem", "safety/trust positioning", "long-context capability"],
        "weaknesses": ["usage limits frustrate heavy users", "plan jump from Pro to Max can feel steep", "model behavior can be conservative", "source grounding requires user-provided context or tools", "feature availability changes quickly"],
        "missing": ["more transparent usage forecasting", "native citation/search layer", "better plan between Pro and Max", "visible memory/context controls", "richer team collaboration inside artifacts"],
        "opportunities": ["artifact-based workspaces", "enterprise reasoning assistant", "Claude as safe agent platform", "long-context knowledge apps", "developer workflow automation"],
        "rating": ["Ease of Use: 9/10", "Features: 9/10", "Performance: 9/10", "Customization: 8/10", "AI: 10/10", "Automation: 7/10", "Integrations: 8/10", "Scalability: 9/10", "Innovation: 9/10", "Value for Money: 8/10", "Overall: 8.7/10"],
    },
]


def source_log(report):
    return "\n".join(f"- [{label}]({url})" for label, url in report["sources"])


def feature_sections(report):
    out = []
    for category in FEATURE_CATEGORIES:
        if category == "Core Features":
            desc = report["features"]
        elif category == "Offline Features":
            desc = "Offline support is limited or not the main value; most capabilities require cloud AI, SaaS APIs, or connected apps."
        elif category == "Mobile Features":
            desc = "Mobile or browser/desktop app availability exists where documented, but exact parity with web/desktop should be verified."
        else:
            desc = f"{category} exist where documented, but exact scope depends on plan, workspace, and current product release."
        out.append(f"### {category}\n- Description: {desc}\n- Why it exists: To make the product operationally useful instead of a one-off AI demo.\n- User benefit: Users get faster output, better control, and more repeatable workflows.\n")
    return "\n".join(out)


def bullets(items):
    return "\n".join(f"- {item}" for item in items)


def make_report(r):
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
- Why does this problem exist? Work is fragmented across sources, apps, teams, and formats, while AI quality depends heavily on context and governance.
- How did people solve this before? {r['before']}
- Why do users choose this product? {r['why']}

## 3. Core Features

{feature_sections(r)}

## 4. Complete User Journey

{r['journey']}

The journey matures from first useful output to trusted daily workflow, then to team/admin/API use where the product supports it.

## 5. Information Architecture

{r['ia']}

Good IA for this category keeps tasks, history, integrations, usage, and governance easy to inspect.

## 6. UX Analysis

{r['ux']}

Strengths are speed and lower friction; weaknesses are hidden limits, trust calibration, and the need to verify AI outputs before business use.

## 7. AI Features

{r['ai']}

AI should be evaluated for grounding, controllability, model transparency, context handling, safety behavior, and failure recovery.

## 8. Technical Analysis

{r['technical']}

Unknowns include internal model routing, ranking, storage architecture, data retention implementation, and evaluation infrastructure unless publicly documented.

## 9. Integrations

{r['integrations']}

Integration value depends on depth, permissions, failure handling, exportability, and whether connected actions are auditable.

## 10. Automation

{r['automation']}

Automation should include clear triggers, actions, approvals, logs, retries, and cost/usage visibility.

## 11. Collaboration

{r['collaboration']}

Collaboration quality should be tested through shared workspaces, roles, comments, version history, analytics, and admin governance.

## 12. Customization

{r['customization']}

Customization is strongest when users can encode brand, process, sources, prompts, and permissions without locking themselves in.

## 13. Security

{r['security']}

Security diligence should include data-use policy, training opt-outs, SSO/SCIM, encryption, audit logs, retention, and connected-app permissions.

## 14. Performance

{r['performance']}

Performance should be measured by correct completed work, not only latency: accuracy, retry behavior, cost, uptime, and output quality all matter.

## 15. Community

{r['community']}

Community evidence is useful for real complaints, but official docs should anchor factual feature claims.

## 16. Strengths

{bullets(r['strengths'])}

## 17. Weaknesses

{bullets(r['weaknesses'])}

## 18. Missing Features

{bullets(r['missing'])}

These features matter because AI users need evidence, controls, and predictable costs before adopting the product as infrastructure.

## 19. Hidden Opportunities

{bullets(r['opportunities'])}

## 20. Reverse Engineering

- Keep: {r['purpose']}
- Redesign: make verification, permissions, cost, and workflow state first-class.
- Remove: opaque limits, hidden model behavior, and claims that cannot be verified.
- Simplify: onboarding, admin setup, integration selection, and failure recovery.

## 21. Competitive Advantages

- Why users stay: history, habits, integrations, trust, templates, APIs, team setup, and accumulated context.
- What creates lock-in: saved workflows, sources, brand knowledge, connected apps, enterprise policies, and generated artifacts.
- Why competitors struggle: they must compete on workflow, trust, and distribution, not just model quality.

## 22. Ideal User

- Who should use it: {r['users']}.
- Who should avoid it: users who need zero-review automation, fixed offline operation, or compliance guarantees not covered by the plan.

## 23. SWOT Analysis

- Strengths: {', '.join(r['strengths'][:3])}.
- Weaknesses: {', '.join(r['weaknesses'][:3])}.
- Opportunities: {', '.join(r['opportunities'][:3])}.
- Threats: bundled platform AI, model commoditization, privacy concerns, pricing pressure, and user fatigue from low-quality AI output.

## 24. Product Rating

{bullets(r['rating'])}

## 25. Lessons Learned

- Best ideas worth keeping: context-aware AI, integrations, citations or governance, reusable workflows, and clear distribution.
- Worst ideas to avoid: opaque pricing, shallow integrations, unverifiable outputs, and weak admin/security defaults.
- Innovations worth adapting: AI becomes more valuable when it is embedded into real workflows and source systems.
- Design principles: expose context, confidence, cost, and control.
- Architecture principles: log everything important, separate retrieval from generation, scope permissions, and design for export.
- Business lessons: defensibility comes from workflow ownership, not generic text generation alone.
- Product strategy lessons: products should evolve from single-task AI into trusted operating layers only after they earn user confidence.
"""


def main():
    for r in REPORTS:
        (ROOT / r["path"]).write_text(make_report(r).rstrip() + "\n", encoding="utf-8")

    registry_path = ROOT / "product-registry.md"
    registry = registry_path.read_text(encoding="utf-8")
    for r in REPORTS:
        registry = registry.replace(f"[{r['path']}]({r['path']}) | Not started |", f"[{r['path']}]({r['path']}) | {r['status']} |")
    registry_path.write_text(registry, encoding="utf-8")

    combined_path = ROOT / "combined/complete-product-research-report.md"
    text = combined_path.read_text(encoding="utf-8")
    marker = "_Remaining product reports will be appended in original registry order as each batch is completed._"
    addition = "\n".join((ROOT / r["path"]).read_text(encoding="utf-8") + "\n---\n" for r in REPORTS)
    text = text.replace(marker, addition + "\n" + marker)
    for r in REPORTS:
        text = text.replace(f"{r['name']}]({r['path']}) - {r['category']} - Not started", f"{r['name']}]({r['path']}) - {r['category']} - {r['status']}")
    combined_path.write_text(text.rstrip() + "\n", encoding="utf-8")

    candidates = ROOT / "discovered-tools/candidates.md"
    ctext = candidates.read_text(encoding="utf-8")
    additions = [
        "| Perplexity Comet | AI browser | Appeared during Perplexity research | Perplexity AI | https://www.perplexity.ai/comet | Important agentic-browser pattern to evaluate separately. |",
        "| Writesonic | AI writing/GTM tool | Appeared in Copy.ai and Jasper competitive context | Jasper AI; Copy.ai | https://writesonic.com/ | Candidate writing and marketing automation competitor. |",
        "| Relevance AI | AI agent platform | Appeared in Zapier/Lindy automation comparisons | Zapier; Lindy | https://relevanceai.com/ | Candidate for agent workforce and no-code automation research. |",
        "| Activepieces | Open-source automation | Appeared in Zapier automation comparisons | Zapier | https://www.activepieces.com/ | Open-source automation alternative worth researching. |",
        "| Bardeen | Browser automation | Appeared in AI automation comparisons | Zapier | https://www.bardeen.ai/ | Useful browser/workflow automation candidate. |",
        "| Anthropic API | Developer AI platform | Appeared in Claude AI research | Claude AI | https://platform.claude.com/docs | Core developer platform adjacent to Claude chat. |",
    ]
    for line in additions:
        if line not in ctext:
            ctext += "\n" + line
    candidates.write_text(ctext.rstrip() + "\n", encoding="utf-8")
    print("Batch 004 reports filled: Perplexity AI, Jasper AI, Copy.ai, Zapier, Claude AI")


if __name__ == "__main__":
    main()
