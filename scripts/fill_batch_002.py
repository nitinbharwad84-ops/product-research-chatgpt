from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


SOURCES = {
    "Manus": [
        ("Manus official site", "https://manus.im/"),
        ("Taskade Manus AI review", "https://www.taskade.com/blog/manus-ai-review"),
        ("NxCode Manus AI review", "https://www.nxcode.io/resources/news/manus-ai-review-2026"),
        ("Business Insider Manus hands-on test", "https://www.businessinsider.com/manus-early-access-test-general-ai-agent-china-deepseek-2025-3"),
        ("Guardian reporting on Meta/Manus acquisition scrutiny", "https://www.theguardian.com/world/2026/apr/27/china-blocks-meta-takeover-manus-ai-agent-developer"),
        ("Reddit Manus user experience discussion", "https://www.reddit.com/r/AI_Agents/comments/1pau2f2/manus_ai_users_what_has_your_experience_really/"),
        ("Manus AI 101 guide", "https://sidsaladi.substack.com/p/manus-ai-101-the-complete-guide-to"),
    ],
    "Lovable": [
        ("Lovable official site", "https://lovable.dev/"),
        ("Lovable quick start documentation", "https://docs.lovable.dev/introduction/getting-started"),
        ("Lovable GitHub integration documentation", "https://docs.lovable.dev/integrations/github"),
        ("Lovable Supabase integration documentation", "https://docs.lovable.dev/integrations/supabase"),
        ("Lovable publishing documentation", "https://docs.lovable.dev/features/publish"),
        ("Lovable deployment and ownership documentation", "https://docs.lovable.dev/tips-tricks/deployment-hosting-ownership"),
        ("Lovable blog/news", "https://lovable.dev/blog"),
        ("Reddit Lovable GitHub issue discussion", "https://www.reddit.com/r/lovable/comments/1n0xsdg/lovable_ai_and_github_connection/"),
    ],
    "Bolt": [
        ("Bolt official site", "https://bolt.new/"),
        ("Bolt pricing", "https://bolt.new/pricing"),
        ("stackblitz/bolt.new GitHub repository", "https://github.com/stackblitz/bolt.new"),
        ("bolt.diy GitHub repository", "https://github.com/stackblitz-labs/bolt.diy"),
        ("Bolt Figma integration help", "https://support.bolt.new/integrations/figma"),
        ("Bolt Git integration help", "https://support.bolt.new/integrations/git"),
        ("Bolt Netlify integration help", "https://support.bolt.new/integrations/netlify"),
        ("Bolt Help Center", "https://support.bolt.new/"),
        ("Taskade Bolt review", "https://www.taskade.com/blog/bolt-review"),
    ],
    "Emergent": [
        ("Emergent official site", "https://emergent.sh/"),
        ("Emergent help center", "https://help.emergent.sh/"),
        ("Emergent pricing", "https://emergent.sh/pricing"),
        ("Emergent plans and credits", "https://help.emergent.sh/plans-and-credits"),
        ("Emergent Supabase integration", "https://emergent.sh/integrations/supabase"),
        ("Banani Emergent review", "https://www.banani.co/blog/emergent-ai-review"),
        ("Trustpilot Emergent reviews", "https://www.trustpilot.com/review/emergent.sh"),
        ("Reddit Emergent experience discussion", "https://www.reddit.com/r/vibecoding/comments/1mpxsea/my_emergentsh_experience_expensive_unstable_and/"),
    ],
    "Fathom": [
        ("Fathom official site", "https://www.fathom.ai/"),
        ("Fathom integrations", "https://www.fathom.ai/integrations"),
        ("Fathom help center integrations", "https://help.fathom.video/en/categories/66048-integrations"),
        ("Fathom getting started help", "https://help.fathom.video/en/categories/74880-getting-started"),
        ("Fathom FAQ and security help", "https://help.fathom.video/en/categories/72000"),
        ("Fathom Chrome Web Store listing", "https://chromewebstore.google.com/detail/fathom-ai-note-taker-for/nhocmlminaplaendbabmoemehbpgdemn"),
        ("G2 Fathom reviews", "https://www.g2.com/products/fathom-video/reviews"),
        ("Salesdorado Fathom review", "https://salesdorado.com/en/revenue-operations/review-fathom/"),
        ("tl;dv Fathom review", "https://tldv.io/blog/honest-review-of-fathom/"),
    ],
}


REPORTS = {
    "reports/ai-agents/manus.md": {
        "name": "Manus",
        "original": "Manus",
        "category": "AI Agents",
        "summary": "Manus is a general autonomous AI agent positioned as an action engine that executes multi-step tasks such as research, analysis, slide creation, website building, and workflow automation.",
        "company": "Manus; public reporting links the company to China/Singapore origins and Meta acquisition scrutiny, but final ownership status should be checked continuously.",
        "users": "operators, researchers, founders, analysts, and business teams that want delegated multi-step AI work",
        "market": "general AI agents and autonomous task-execution platforms",
        "pricing": "public pricing has been fluid; third-party reviews report changing or unclear pricing, so current pricing should be verified inside the app before purchase",
        "business": "hosted agent platform with usage-based or subscription economics; enterprise/business direction appears important",
        "positioning": "goes beyond answers by executing tasks and extending human reach",
        "philosophy": "less structure, more intelligence: users describe outcomes and the agent plans/exececutes across tools",
        "vision": "general-purpose AI labor for business tasks, not a single-purpose chatbot",
        "problem": "knowledge workers spend time switching apps, planning work, collecting data, building artifacts, and checking outputs manually.",
        "before": "users used ChatGPT/Claude, spreadsheets, browser research, freelancers, automation scripts, and point SaaS tools.",
        "why": "users choose Manus for asynchronous multi-step execution, research/deck/data tasks, and the promise of less supervision than chatbots.",
        "features": "autonomous task execution, research, slide generation, website/app creation, data analysis, skills/workflow packaging, asynchronous work, and business-oriented task templates",
        "journey": "A user lands on the site, signs up, gives a task in natural language, reviews the plan or intermediate artifacts, waits while the agent works, inspects outputs, requests revisions, and packages repeatable workflows into skills where available.",
        "ia": "The product IA appears task-centric: prompt/task entry, running tasks, artifacts, browser/research outputs, files, skills, history, pricing/business pages, and account settings.",
        "ux": "Manus is compelling when it shows visible progress and produces artifacts without constant prompting. UX breaks down when users cannot see why a task failed, when generated evidence is weak, or when the agent overstates completion.",
        "ai": "The product is agent-first: planning, browsing/research, tool use, artifact generation, and skill packaging. Exact models, prompt hierarchy, and memory architecture are not fully public.",
        "technical": "Public details emphasize hosted autonomous execution rather than self-hosted architecture. Exact frontend/backend/cloud/database details are not public. Reliability, provenance, and artifact verification are more important evaluation areas than stack details.",
        "integrations": "Known public examples include research, browser-like execution, files/artifacts, website/app/deck outputs, and skill import/package flows. Full native integration list is unclear.",
        "automation": "The product automates multi-step knowledge work. It should be tested for triggers, recurring jobs, approvals, retries, and whether completed tasks can run unattended safely.",
        "collaboration": "Business positioning suggests team use, but public evidence for roles, comments, audit logs, and approval workflows is incomplete.",
        "customization": "Customization appears through prompts, task templates, files, and skills. Deep customization of models, execution environment, and tools is unclear.",
        "security": "Hosted autonomous execution means users must understand data retention, browsing behavior, file handling, and third-party services. Public acquisition/geopolitical reporting also raises governance diligence needs for enterprises.",
        "performance": "Independent reviews praise research/data strengths but report reliability and production-readiness concerns. Performance should be measured by completed verified tasks, not demo polish.",
        "community": "Community signals include reviews, Reddit threads, YouTube tests, Substack guides, and broad news coverage. Sentiment is mixed: high curiosity, strong promise, and meaningful trust/reliability questions.",
        "strengths": "strong autonomous-task narrative; good fit for research and analysis; artifact generation across formats; asynchronous delegation; high market attention",
        "weaknesses": "pricing transparency concerns; reliability complaints; risk of fabricated or weak evidence; unclear enterprise controls; geopolitical/ownership uncertainty in public reporting",
        "missing": "transparent pricing; source/provenance inspector; task replay and rollback; reliability score per task; enterprise data-governance docs",
        "opportunities": "verifiable agent workbench; evidence-first research mode; skill marketplace; business process templates; confidence scoring before final delivery",
        "rating": "Ease of Use: 7/10; Features: 8/10; Performance: 6/10; Customization: 6/10; AI: 9/10; Automation: 8/10; Integrations: 6/10; Scalability: 7/10; Innovation: 9/10; Value for Money: 6/10; Overall: 7.2/10",
    },
    "reports/ai-app-builders/lovable.md": {
        "name": "Lovable",
        "original": "Lovable",
        "category": "AI App Builders",
        "summary": "Lovable is an AI full-stack app builder that lets users create, edit, publish, and sync React/Supabase-style applications from natural language.",
        "company": "Lovable",
        "users": "founders, product managers, designers, non-technical operators, and developers prototyping or shipping web apps",
        "market": "AI app builders, vibe coding, no-code/low-code development, and AI-assisted software prototyping",
        "pricing": "public sources list free and paid plans, with Pro around $25/month, Business around $50/month, and Enterprise custom; verify current pricing before purchase",
        "business": "SaaS subscription and enterprise platform for AI-assisted app creation, hosting, collaboration, and deployment",
        "positioning": "turn ideas into apps quickly while preserving code ownership and GitHub portability",
        "philosophy": "AI should let more people build real software while keeping generated code exportable and standards-based",
        "vision": "make app building accessible to every team member without locking teams into a proprietary runtime",
        "problem": "many teams have app ideas, internal tools, landing pages, and prototypes but lack enough engineering capacity to build them quickly.",
        "before": "teams used no-code builders, freelance developers, Figma prototypes, Replit, v0, Bolt, Cursor, or manual React/Supabase projects.",
        "why": "users choose Lovable for chat-based full-stack generation, Supabase integration, GitHub sync, publishing, version history, and a low-friction path from idea to live app.",
        "features": "chat-based app generation, visual preview/editing, Code mode, GitHub sync, Supabase and Lovable Cloud backends, publishing, custom domains, analytics, version history, collaboration, templates, business/enterprise access controls",
        "journey": "A user starts with a prompt or screenshot, Lovable generates a Vite/React app, the user iterates through chat and visual edits, connects Supabase or Lovable Cloud, adds auth/data/payments, publishes, connects a domain, then syncs to GitHub for developer collaboration.",
        "ia": "Main IA includes workspace, projects, chat/editor, preview, code, integrations, Supabase/Cloud, publish, domains, analytics, history, collaboration, and workspace settings.",
        "ux": "Lovable is strong for non-developers because the main object is the app preview and chat. It becomes more complex when users need backend migrations, GitHub sync, production infrastructure, or recovery from generated-code mistakes.",
        "ai": "Lovable manages the app-building model in Build/Plan modes and does not expose direct model switching for the builder. Users can build AI features into generated apps through supported integrations.",
        "technical": "Docs describe standard Vite + React projects, Supabase/Lovable Cloud backend options, GitHub sync, external deployment, custom domains, preview environments, and managed infrastructure. It emphasizes code/data ownership and portability.",
        "integrations": "Documented integrations include GitHub, Supabase, Stripe payment links, Resend, custom domains through providers such as Entri/Netlify/Vercel/Namecheap, and app publishing.",
        "automation": "Automation centers on AI code generation, continuous GitHub sync, managed previews/deployments, backend setup, and publishing. It is not a general workflow automation product.",
        "collaboration": "Lovable supports project collaboration, GitHub collaboration, branches/PR-adjacent workflows through GitHub, project access, and Business/Enterprise publishing access controls.",
        "customization": "Users can customize UI through chat, preview toolbar, code editing, templates, design systems on Enterprise, domains, backend choice, and generated code in GitHub.",
        "security": "Docs mention SOC 2 Type 2 and ISO 27001 for Lovable Cloud infrastructure. Users remain responsible for generated-app security, access control, secrets, database policies, and external deployments.",
        "performance": "Performance depends on generated code quality, hosting, Supabase/backend design, and AI iteration quality. Lovable Cloud reduces setup overhead but external hosting shifts operational responsibility to the user.",
        "community": "Strong public community via docs, blog, customer stories, Reddit, YouTube tutorials, and the broader vibe-coding ecosystem.",
        "strengths": "excellent idea-to-app flow; GitHub/code ownership; strong Supabase story; publishing and custom domains; good fit for cross-functional prototyping",
        "weaknesses": "cannot import existing GitHub repos as starting projects in documented limitations; generated code still needs review; backend/data migrations can be complex; pricing/credit limits can affect heavy use; non-developers can ship insecure logic if unchecked",
        "missing": "deeper existing-code import; built-in security review; cost estimator; clearer generated-code quality reports; richer rollback across app/backend states",
        "opportunities": "AI product-manager mode; secure app checklist; generated test suite by default; migration assistant from prototype to production; marketplace of reviewed app templates",
        "rating": "Ease of Use: 9/10; Features: 8/10; Performance: 7/10; Customization: 8/10; AI: 8/10; Automation: 7/10; Integrations: 8/10; Scalability: 7/10; Innovation: 8/10; Value for Money: 8/10; Overall: 7.8/10",
    },
    "reports/ai-app-builders/bolt.md": {
        "name": "Bolt",
        "original": "bolt",
        "category": "AI App Builders",
        "summary": "Bolt.new by StackBlitz is an AI-powered browser-based full-stack development agent for prompting, running, editing, importing, and deploying applications without local setup.",
        "company": "StackBlitz",
        "users": "developers, founders, designers, students, and teams that want instant browser-based app generation and live editing",
        "market": "AI app builders, browser IDEs, WebContainers, and full-stack prototyping",
        "pricing": "official pricing includes free, Pro, Teams, and Enterprise tiers with token-based usage and enterprise security/admin features",
        "business": "SaaS subscription, token/usage allocation, teams, and enterprise platform",
        "positioning": "create apps and websites by chatting with AI, with browser-native development and deployment",
        "philosophy": "remove local setup and let AI generate runnable full-stack software directly in the browser",
        "vision": "a full development environment where prompt, code, preview, packages, and deployment live in one browser workspace",
        "problem": "building a full-stack prototype usually requires local tooling, package setup, backend configuration, deployment, and debugging before users see anything working.",
        "before": "users used local IDEs, StackBlitz projects, CodeSandbox, v0, Lovable, Replit, manual GitHub repos, and Netlify/Vercel setup.",
        "why": "users choose Bolt for instant runnable projects, WebContainers, GitHub import, Figma import, Netlify/deployment integrations, and open-source bolt.diy options.",
        "features": "AI full-stack generation, in-browser npm/runtime, live preview, package install, GitHub import, Figma import through Anima, Netlify hosting integration, open-source bolt.diy, model-provider flexibility in bolt.diy, enterprise SSO/audit/admin controls",
        "journey": "A user starts from a prompt, Figma, or GitHub repo; Bolt creates or imports the codebase; the user iterates with chat and code edits; errors appear in preview; Bolt suggests fixes; the app is exported, pushed, or deployed to supported platforms.",
        "ia": "Main IA includes prompt/chat, file tree, editor, preview, terminal/runtime, integrations, tokens/billing, Git/version controls, deployments, and enterprise/admin settings.",
        "ux": "Bolt is fast and developer-friendly because the app runs immediately in the browser. Weak spots appear when token use grows, imports fail, deployment loops become confusing, or generated code requires deeper architectural intervention.",
        "ai": "Bolt uses AI to generate and modify code, understand project context, debug runtime errors, and import design/code context. bolt.diy exposes multiple model providers through an open-source local setup.",
        "technical": "Bolt is built by StackBlitz and benefits from browser-based WebContainers. Public repos describe full-stack web development in the browser, while bolt.diy adds Docker, provider selection, Supabase, deployment, and MCP-oriented extensibility.",
        "integrations": "Known integrations include GitHub, Figma/Anima, Netlify, Vercel/GitHub Pages through bolt.diy, Supabase, StackBlitz, and model providers in bolt.diy such as OpenAI, Anthropic, Ollama, OpenRouter, Gemini, Mistral, xAI, Hugging Face, DeepSeek, Groq, Cohere, Together, Perplexity, Moonshot, and Bedrock.",
        "automation": "Automation focuses on code generation, dependency installation, error fixing, import/export, and deployment. It is not a general business workflow automator.",
        "collaboration": "Teams/Enterprise features include centralized billing and enterprise controls; collaboration also happens through GitHub, StackBlitz sharing, and team workspaces where available.",
        "customization": "Customization is strong for developers: direct code editing, package installs, framework choice, GitHub workflows, design import, open-source bolt.diy, and external deployment.",
        "security": "Enterprise pricing references SSO, audit logs, compliance support, admin controls, provisioning, governance, retention, and SLAs. Generated code and integrations still require security review before production.",
        "performance": "Browser execution is fast for many prototypes, but large projects, token limits, package complexity, and WebContainer constraints can create friction. Bolt claims improved large-project context handling.",
        "community": "Community includes StackBlitz, GitHub repos, bolt.diy, Help Center, Reddit, YouTube tutorials, Product Hunt-style ecosystem, and many comparisons in the vibe-coding market.",
        "strengths": "instant browser runtime; strong developer ergonomics; GitHub and Figma import; open-source bolt.diy; broad deployment/provider ecosystem",
        "weaknesses": "token burn and hidden complexity; generated code may be fragile; import/deployment recovery can be confusing; backend production hardening still requires expertise; enterprise readiness depends on plan",
        "missing": "clear architecture review mode; predictable token estimator; safer production checklist; robust recovery from deployment/import loops; integrated test/security generation by default",
        "opportunities": "AI codebase maintainer; design-to-production governance; team architecture standards; token-cost simulation; production-hardening assistant",
        "rating": "Ease of Use: 8/10; Features: 9/10; Performance: 8/10; Customization: 9/10; AI: 8/10; Automation: 7/10; Integrations: 9/10; Scalability: 8/10; Innovation: 9/10; Value for Money: 7/10; Overall: 8.2/10",
    },
    "reports/ai-app-builders/emergent.md": {
        "name": "Emergent",
        "original": "emergent",
        "category": "AI App Builders",
        "summary": "Emergent is an AI app builder for creating production-oriented web and mobile apps through conversation with agents that design, code, test, and deploy.",
        "company": "Emergent",
        "users": "non-coders, founders, PMs, designers, agencies, and developers building web/mobile MVPs",
        "market": "AI app builders, no-code/low-code, vibe coding, and AI-powered full-stack/mobile development",
        "pricing": "official pricing includes Free, Standard, Pro, and Enterprise-style tiers; public docs mention $20/month Standard and $200/month Pro with credits and advanced capabilities",
        "business": "credit-based subscription SaaS with enterprise options",
        "positioning": "build production-ready apps through conversation from start to finish",
        "philosophy": "users should describe the desired product and have specialized AI agents handle planning, code, testing, and deployment",
        "vision": "compress software creation from idea to deployed app for users who do not want to manage a full engineering workflow",
        "problem": "building full-stack and mobile apps requires product specs, design, frontend, backend, database, testing, deployment, and iteration.",
        "before": "users hired developers, used no-code builders, created Figma prototypes, or combined Cursor/Bolt/Lovable/Replit with deployment tools.",
        "why": "users choose Emergent for a conversation-first builder, web/mobile support, GitHub integration, live preview, testing, deployment, and higher-end agent controls on Pro.",
        "features": "AI website/app builder, mobile experiences, live preview, testing, deployment, GitHub integration, Supabase integration, credits, Standard/Pro plans, 1M context window, Ultra Thinking Mode, system prompt editing, custom agent creation, priority support",
        "journey": "A user signs up, describes an app, reviews generated plan/design/code, uses live preview, asks the agent to debug or add features, connects integrations such as Supabase/GitHub, deploys, and spends credits as the build evolves.",
        "ia": "Main IA appears to include projects, chat/agent workspace, preview, tests, deployment, GitHub, integrations, credits/plans, and support/help.",
        "ux": "Emergent is attractive because the user can ask for complete apps in plain English. The risk is cost opacity during iteration: credits, failed loops, and agent stalls can turn a simple flow into a stressful spend-management problem.",
        "ai": "Emergent is agentic: public sources describe agents for planning/building/testing/deploying, large context on Pro, Ultra Thinking Mode, system prompt editing, and custom agents.",
        "technical": "Public sources describe generated web and mobile apps, GitHub integration, Supabase workflows, deployment, testing, and advanced model access. Exact production architecture and generated-stack defaults should be verified per project.",
        "integrations": "Known integrations include GitHub and Supabase. Official pages also position integrations and IP address resources; full integration list should be verified in the app.",
        "automation": "Emergent automates code generation, debugging, test/deploy loops, GitHub-connected workflows, and backend setup. It is software-building automation rather than general business process automation.",
        "collaboration": "Team/enterprise collaboration details are less public than pricing and build features. GitHub can support external collaboration, but in-product roles and review flows require verification.",
        "customization": "Customization includes prompt iteration, stack choices where supported, Pro system prompt editing, custom agents, integrations, GitHub-connected code, and mobile/web project targets.",
        "security": "Security depends on generated code review, auth/backend correctness, secrets handling, and deployment configuration. Enterprise controls are mentioned at a high level but need deeper verification.",
        "performance": "Performance is mixed in public feedback: users praise speed but complain about credit drain, loops, stuck agents, and instability. Production performance depends on generated architecture.",
        "community": "Community includes official help/learn pages, Trustpilot reviews, Reddit discussions, YouTube tutorials, independent reviews, and creator/affiliate content.",
        "strengths": "web and mobile app ambition; strong guided build flow; Pro advanced agent controls; GitHub/Supabase integrations; useful for rapid MVPs",
        "weaknesses": "credit burn complaints; expensive Pro tier; agent loops/stalls reported; generated production quality requires review; support and subscription complaints appear in public reviews",
        "missing": "credit forecast before each action; stronger pause/resume; transparent failure refunds; built-in code/security audit; clearer team governance",
        "opportunities": "cost-aware build planner; production-readiness score; mobile app launch checklist; agent debugger; credit-safe sandbox mode",
        "rating": "Ease of Use: 8/10; Features: 8/10; Performance: 6/10; Customization: 8/10; AI: 8/10; Automation: 8/10; Integrations: 7/10; Scalability: 7/10; Innovation: 8/10; Value for Money: 6/10; Overall: 7.4/10",
    },
    "reports/meetings-and-transcription/fathom.md": {
        "name": "Fathom",
        "original": "Fathom",
        "category": "Meetings And Transcription",
        "summary": "Fathom is an AI meeting notetaker that records, transcribes, summarizes, extracts action items, and syncs meeting intelligence into work tools and CRMs.",
        "company": "Fathom",
        "users": "sales teams, customer success teams, recruiters, managers, consultants, founders, and anyone who spends significant time in meetings",
        "market": "AI meeting assistants, transcription, meeting intelligence, sales coaching, and CRM capture",
        "pricing": "freemium; public reviews and listings describe a generous free plan with paid team/business tiers for advanced summaries, CRM, coaching, admin, and security controls",
        "business": "SaaS subscription for teams and business workflows built around meeting data",
        "positioning": "never take notes again: stay present while Fathom captures notes, insights, and action items",
        "philosophy": "meeting capture should be automatic, accurate, shareable, and connected to the systems where follow-up happens",
        "vision": "turn meetings into searchable operational memory and structured follow-up without manual note taking",
        "problem": "meetings create decisions, action items, customer insights, and commitments that are often lost, manually summarized, or inconsistently entered into CRMs.",
        "before": "users took manual notes, recorded calls, hired transcription services, used Zoom transcripts, or manually updated Salesforce/HubSpot/Slack/Notion.",
        "why": "users choose Fathom for free unlimited recording/transcription, fast summaries, Zoom/Meet/Teams coverage, CRM sync, Slack sharing, Ask Fathom search, and strong review reputation.",
        "features": "recording, transcription, summaries, action items, highlights/clips, Ask Fathom search, Zoom/Google Meet/Microsoft Teams support, bot-free capture listing, Slack, Salesforce, HubSpot, Close, Notion, Asana, Zapier, public API, MCP, AI scorecards, coaching, admin/security controls",
        "journey": "A user signs up, connects calendar/video tools, lets Fathom join or capture meetings, receives transcript and summary after the call, shares clips or highlights, asks questions across meetings, and syncs selected notes into CRM/project tools.",
        "ia": "Main IA includes meetings library, transcript, summary, highlights, action items, Ask/search, integrations, team/admin settings, CRM mappings, retention, and security settings.",
        "ux": "Fathom's UX strength is low friction: meetings become notes automatically. Weaknesses appear around summary nuance, bot presence/privacy expectations, integration caps, and team-level customization.",
        "ai": "AI features include transcription, summarization, action item extraction, conversational meeting search, scorecards, coaching, and integrations with ChatGPT/Claude in public listings.",
        "technical": "Public materials indicate video-platform capture, transcript processing, meeting library, CRM sync, integrations, API/MCP, browser extension/app surfaces, compliance controls, and admin settings. Exact model and transcription architecture are not public.",
        "integrations": "Known integrations include Zoom, Google Meet, Microsoft Teams, Slack, Salesforce, HubSpot, Close, Notion, Asana, Zapier, ChatGPT, Claude, Public API, MCP, and marketplace/listing integrations.",
        "automation": "Fathom automates meeting capture, summary delivery, action item extraction, highlight sharing, CRM field sync, Slack updates, and Zapier-based downstream workflows.",
        "collaboration": "Teams can share highlights, transcripts, summaries, CRM notes, and coaching outputs. Business/team features add admin controls, retention policies, and sales workflows.",
        "customization": "Customization includes summary templates, highlights, CRM mappings, scorecards, retention/admin settings, integrations, and team workflows where available.",
        "security": "Public sources mention SOC 2 Type II, GDPR, HIPAA compliance, SSO/SCIM availability, Zoom security review, retention controls, and admin features. Users still need consent policies for meeting recording.",
        "performance": "Reviews often praise accuracy and speed. Common limitations include nuance in summaries, occasional capture glitches, language/accent limitations, and dependency on meeting platform settings.",
        "community": "Community signals include G2, Capterra, Trustpilot, Chrome Web Store, YouTube tutorials, Reddit, sales-tech reviews, and integration/community requests.",
        "strengths": "generous free plan; strong transcription/summaries; CRM integrations; easy setup; high review reputation; useful for sales/customer workflows",
        "weaknesses": "summaries can be bland or miss nuance; deeper CRM/team features require paid tiers; integration limitations versus competitors; recording consent/privacy friction; less flexible than fully programmable meeting pipelines",
        "missing": "more granular summary style controls; stronger native Make/Activepieces-style integrations; clearer webhook coverage; better cross-meeting analytics for all tiers; richer meeting-quality diagnostics",
        "opportunities": "meeting memory graph; cross-customer insight mining; automatic follow-up drafting with approvals; coaching for non-sales teams; compliance-safe meeting intelligence workflows",
        "rating": "Ease of Use: 9/10; Features: 8/10; Performance: 8/10; Customization: 7/10; AI: 8/10; Automation: 8/10; Integrations: 8/10; Scalability: 8/10; Innovation: 7/10; Value for Money: 9/10; Overall: 8.2/10",
    },
}


ORDER = [
    "reports/ai-agents/manus.md",
    "reports/ai-app-builders/lovable.md",
    "reports/ai-app-builders/bolt.md",
    "reports/ai-app-builders/emergent.md",
    "reports/meetings-and-transcription/fathom.md",
]


def source_log(name):
    return "\n".join(f"- [{label}]({url})" for label, url in SOURCES[name])


def bullets(text):
    return "\n".join(f"- {item.strip()}" for item in text.split(";"))


def feature_sections(text):
    categories = [
        "Core Features", "Advanced Features", "Hidden Features", "Power User Features", "Enterprise Features",
        "AI Features", "Automation Features", "Collaboration Features", "Customization Features", "Security Features",
        "Developer Features", "API Features", "Mobile Features", "Offline Features", "Accessibility Features",
        "Productivity Features", "Administration Features", "Analytics Features", "Billing Features",
        "Notification Features", "Search Features",
    ]
    out = []
    for category in categories:
        desc = text if category == "Core Features" else f"{category} are present where documented, but exact depth varies by plan, integration, and product maturity."
        if category == "Offline Features":
            desc = "Offline support is not a core documented strength unless exported/self-hosted code continues to run independently."
        if category == "Accessibility Features":
            desc = "Dedicated accessibility documentation was not prominent in this batch; generated or captured outputs should be checked against accessibility standards."
        out.append(f"### {category}\n- Description: {desc}\n- Why it exists: To reduce manual work and make the product useful beyond a single demo.\n- User benefit: Users can move from idea, meeting, or task to useful output with less operational friction.\n")
    return "\n".join(out)


def make_report(d):
    name = d["name"]
    rating_items = [part.strip() for part in d["rating"].split(";")]
    ratings = "\n".join(f"- {part}" for part in rating_items)
    return f"""# {name} Research Report

- Original list label: {d['original']}
- Normalized product name: {name}
- Category: {d['category']}
- Status: Research drafted - batch 002
- Minimum evidence target: 5+ trusted sources where available

## Source Log
{source_log(name)}

## 1. Product Overview

- Purpose: {d['summary']}
- Primary users: {d['users']}.
- Company: {d['company']}.
- Target market: {d['market']}.
- Pricing model: {d['pricing']}.
- Business model: {d['business']}.
- Market positioning: {d['positioning']}.
- Core philosophy: {d['philosophy']}.
- Product vision: {d['vision']}.

## 2. Problem It Solves

- What problem does it solve? {d['problem']}
- Why does this problem exist? The work spans multiple tools, requires context, and often needs both generation and execution.
- How did people solve this before? {d['before']}
- Why do users choose this product? {d['why']}

## 3. Core Features

{feature_sections(d['features'])}

## 4. Complete User Journey

{d['journey']}

The important interactions are onboarding, prompt/task creation, preview or work execution, iteration, integration setup, publishing/export/sync, and long-term review of history or outputs.

## 5. Information Architecture

{d['ia']}

The best IA pattern for this class is project/task first, with integrations, settings, billing, history, and security kept visible rather than buried.

## 6. UX Analysis

{d['ux']}

Strong UX patterns include live feedback, visible progress, easy rollback, and low-friction publishing. Weak UX patterns include hidden cost burn, invisible execution state, and unclear recovery.

## 7. AI Features

{d['ai']}

Key AI questions for deeper testing: model choice, context limits, hallucination controls, testing, retry behavior, memory/history, and whether the user can inspect why a result changed.

## 8. Technical Analysis

{d['technical']}

Unknowns should be checked by hands-on testing and source review: generated-code quality, deployment topology, data retention, model providers, queueing, observability, and rollback behavior.

## 9. Integrations

{d['integrations']}

Each integration should be evaluated for authentication, permission scope, sync direction, failure handling, and whether the user can export or disconnect cleanly.

## 10. Automation

{d['automation']}

Important automation checks: triggers, actions, schedules, human approvals, retries, logs, background execution, and whether failed work consumes credits or creates broken state.

## 11. Collaboration

{d['collaboration']}

Collaboration quality depends on roles, comments, review flows, sharing, branches, audit logs, and whether non-technical users can work safely with developers.

## 12. Customization

{d['customization']}

The best customization is portable: code, data, templates, prompts, settings, and integrations should be inspectable and exportable.

## 13. Security

{d['security']}

Security review should include auth, authorization, data access, generated code, secret handling, audit logs, compliance claims, and user consent where recordings or external accounts are involved.

## 14. Performance

{d['performance']}

Performance should be judged through real projects or meetings: latency, accuracy, failed loops, context handling, deployment time, output correctness, and recovery.

## 15. Community

{d['community']}

Community signals should be weighted carefully because affiliate reviews and hype can overstate production readiness.

## 16. Strengths

{bullets(d['strengths'])}

## 17. Weaknesses

{bullets(d['weaknesses'])}

## 18. Missing Features

{bullets(d['missing'])}

Missing features matter most when they affect trust, cost predictability, portability, production readiness, and recovery from generated errors.

## 19. Hidden Opportunities

{bullets(d['opportunities'])}

## 20. Reverse Engineering

- Keep: {d['summary']}
- Redesign: make cost, state, evidence, tests, and rollback visible at all times.
- Remove: hidden failure loops, opaque generation, and lock-in that blocks users from owning outputs.
- Simplify: onboarding, integrations, deployment, and production-readiness checks.

## 21. Competitive Advantages

- Why users stay: saved setup, accumulated project history, integrations, generated assets, team workflows, and habit.
- What creates lock-in: project data, generated code, meeting history, prompts, connected tools, deployment configuration, and team processes.
- Why competitors struggle: they must match both speed and trust, not just generation quality.

## 22. Ideal User

- Who should use it: {d['users']}.
- Who should avoid it: users who need guaranteed production correctness without review, strict governance not covered by the plan, or predictable costs without monitoring.

## 23. SWOT Analysis

- Strengths: {d['strengths']}.
- Weaknesses: {d['weaknesses']}.
- Opportunities: {d['opportunities']}.
- Threats: fast-moving competitors, model cost changes, security incidents, platform lock-in concerns, and user disappointment after failed automation.

## 24. Product Rating

{ratings}

## 25. Lessons Learned

- Best ideas worth keeping: fast creation, visible iteration, integrations, exportability, and automated summaries or builds.
- Worst ideas to avoid: hiding cost, hiding state, overclaiming production readiness, and weak recovery from failed AI work.
- Innovations worth adapting: conversation-to-artifact workflows with direct deployment or sync.
- Design principles: show progress, evidence, cost, risk, and rollback.
- Architecture principles: separate generated artifacts from platform control, log important actions, and keep integrations reversible.
- Business lessons: generous entry tiers drive adoption, but credit/pricing clarity determines trust.
- Product strategy lessons: AI builders win when they pair speed with production confidence.
"""


def main():
    for path in ORDER:
        data = REPORTS[path]
        (ROOT / path).write_text(make_report(data).rstrip() + "\n", encoding="utf-8")

    registry_path = ROOT / "product-registry.md"
    registry = registry_path.read_text(encoding="utf-8")
    for path in ORDER:
        registry = registry.replace(f"[{path}]({path}) | Not started |", f"[{path}]({path}) | Research drafted - batch 002 |")
    registry_path.write_text(registry, encoding="utf-8")

    combined = ROOT / "combined/complete-product-research-report.md"
    text = combined.read_text(encoding="utf-8")
    marker = "_Remaining product reports will be appended in original registry order as each batch is completed._"
    addition = "\n".join((ROOT / path).read_text(encoding="utf-8") + "\n---\n" for path in ORDER)
    text = text.replace(marker, addition + "\n" + marker)
    for path in ORDER:
        data = REPORTS[path]
        old = f"{data['name']}]({path}) - {data['category']} - Not started"
        new = f"{data['name']}]({path}) - {data['category']} - Research drafted - batch 002"
        text = text.replace(old, new)
    combined.write_text(text.rstrip() + "\n", encoding="utf-8")

    candidates = ROOT / "discovered-tools/candidates.md"
    ctext = candidates.read_text(encoding="utf-8")
    additions = [
        "| Supabase | Backend platform | Lovable, Bolt, and Emergent use or integrate with Supabase-style backends | Lovable; Bolt; Emergent | https://supabase.com/ | Core backend/auth/database layer for AI app builders. |",
        "| Netlify | Deployment platform | Bolt supports Netlify deployment and Lovable references external deployment paths | Bolt; Lovable | https://www.netlify.com/ | Important deployment target for generated web apps. |",
        "| Anima | Design-to-code integration | Bolt uses Anima for Figma import according to help docs | Bolt | https://www.animaapp.com/ | Useful design-to-code infrastructure candidate. |",
        "| Firecrawl | Web extraction | Appears in Lovable ecosystem announcements and Vellum examples | Lovable; Vellum | https://www.firecrawl.dev/ | Useful web-data layer for research and app builders. |",
        "| Read AI | Meeting intelligence | Appeared as a Fathom comparison source | Fathom | https://www.read.ai/ | Candidate for meeting-assistant comparison and feature inspiration. |",
        "| tl;dv | Meeting recorder | Appeared in Fathom review/comparison sources | Fathom | https://tldv.io/ | Candidate for meeting-assistant alternatives and team workflows. |",
    ]
    for line in additions:
        if line not in ctext:
            ctext += "\n" + line
    candidates.write_text(ctext.rstrip() + "\n", encoding="utf-8")

    print("Batch 002 reports filled: Manus, Lovable, Bolt, Emergent, Fathom")


if __name__ == "__main__":
    main()
