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
        "path": "reports/media-generation/adobe-firefly.md",
        "name": "Adobe Firefly",
        "original": "Adobe Firefly",
        "category": "Media Generation",
        "status": "Research drafted - batch 006",
        "sources": [
            ("Adobe Firefly business approach", "https://business.adobe.com/products/firefly-business/firefly-ai-approach.html"),
            ("Adobe Firefly official app", "https://firefly.adobe.com/"),
            ("Adobe Firefly API", "https://developer.adobe.com/firefly-services/"),
            ("Adobe Creative Cloud pricing", "https://www.adobe.com/creativecloud/plans.html"),
            ("SaaS CRM Review Firefly review", "https://saascrmreview.com/adobe-firefly-review/"),
            ("SudoMock Firefly API pricing", "https://sudomock.com/blog/adobe-firefly-api-pricing-2026"),
            ("Reddit Adobe Firefly criticism", "https://www.reddit.com/r/Adobe/comments/1iq7857/adobe_firefly_is_a_scam/"),
        ],
        "purpose": "Adobe Firefly is Adobe's commercially oriented generative AI system for image, video, audio, vector, design, and creative editing workflows across Adobe apps and APIs.",
        "company": "Adobe",
        "users": "designers, marketers, agencies, enterprises, creators, video editors, illustrators, and Creative Cloud users",
        "market": "commercial-safe generative AI, creative suites, image/video generation, and enterprise creative production",
        "pricing": "free and paid Adobe/Firefly plans using generative credits, plus enterprise/API pricing and Creative Cloud bundle access",
        "business": "subscription, Creative Cloud expansion, enterprise licensing, API usage, and generative-credit monetization",
        "positioning": "commercially safe generative AI integrated into professional creative workflows",
        "philosophy": "creative AI should be responsible, commercially usable, and embedded in tools creators already use",
        "vision": "make generative AI a trusted production layer across Adobe's creative ecosystem",
        "problem": "creative teams need faster asset production but face legal, brand, quality, and workflow risks with generic image generators.",
        "before": "stock sites, Photoshop/Illustrator/Premiere manual work, agencies, Midjourney, Stable Diffusion, DALL-E, and outsourced production.",
        "why": "users choose Firefly for Adobe integration, commercial-safety positioning, IP indemnification on qualifying plans, and enterprise trust.",
        "features": "text-to-image, generative fill, generative expand, text effects, vector/style tools, video/audio generation, Photoshop/Illustrator/Premiere/Express integration, APIs, brand-safe workflows, content credentials, and enterprise controls",
        "journey": "A user opens Firefly or an Adobe app, writes a prompt or selects content, generates variants, edits/refines inside Adobe tooling, exports to campaign assets, or automates generation through Firefly Services/API.",
        "ia": "IA spans Firefly web, Creative Cloud apps, generative credit/billing, Adobe Stock/assets, APIs, admin console, and enterprise trust resources.",
        "ux": "Firefly is strong when users stay inside Adobe workflows. Friction appears around credit consumption, output quality versus specialist generators, and Adobe account/subscription complexity.",
        "ai": "AI includes Adobe generative models for image, vector, video, and audio-oriented tasks. Model training and commercial-safety claims are central to positioning, though exact model details are not fully public.",
        "technical": "Adobe provides hosted generation and Firefly Services APIs integrated with Creative Cloud. Content credentials, enterprise controls, and indemnification terms are key technical-commercial differentiators.",
        "integrations": "Deep Adobe ecosystem integration plus API access; external integration is mainly through Firefly Services and enterprise creative pipelines.",
        "automation": "Automation comes through generative edits, batch/API generation, template workflows, and Adobe creative pipelines.",
        "collaboration": "Collaboration flows through Creative Cloud, Adobe Express, libraries, teams, enterprise admin, and brand workflows.",
        "customization": "Customization includes prompts, styles, references, brand assets, Adobe app editing, APIs, and enterprise workflow controls.",
        "security": "Adobe emphasizes responsible development, commercial safety, content credentials, enterprise controls, and indemnification on qualifying plans; users must verify terms by plan.",
        "performance": "Best for safe production-adjacent creative tasks, weaker when users need frontier artistic quality or exact prompt control compared with specialist tools.",
        "community": "Large Adobe ecosystem, tutorials, enterprise creative users, Reddit criticism, YouTube reviews, and API/creative automation coverage.",
        "strengths": ["Adobe ecosystem integration", "commercial-safety positioning", "enterprise trust", "professional editing handoff", "API/services path"],
        "weaknesses": ["credit confusion", "output quality complaints", "subscription complexity", "less open than local models", "commercial-safe framing does not guarantee brand-fit"],
        "missing": ["clearer per-output cost preview", "better creative control", "transparent model/version controls", "stronger prompt audit", "simpler API pricing"],
        "opportunities": ["brand-safe campaign generator", "creative ops automation", "asset localization at scale", "AI production QA", "rights-aware media pipeline"],
        "rating": ["Ease of Use: 8/10", "Features: 9/10", "Performance: 8/10", "Customization: 8/10", "AI: 8/10", "Automation: 8/10", "Integrations: 9/10", "Scalability: 9/10", "Innovation: 8/10", "Value for Money: 7/10", "Overall: 8.2/10"],
    },
    {
        "path": "reports/voice-and-audio/elevenlabs.md",
        "name": "ElevenLabs",
        "original": "ElevenLabs",
        "category": "Voice And Audio",
        "status": "Research drafted - batch 006",
        "sources": [
            ("ElevenLabs official site", "https://elevenlabs.io/"),
            ("ElevenLabs API pricing", "https://elevenlabs.io/pricing/api"),
            ("ElevenLabs docs", "https://elevenlabs.io/docs"),
            ("ElevenLabs safety", "https://elevenlabs.io/safety"),
            ("BigVu ElevenLabs pricing guide", "https://bigvu.tv/blog/elevenlabs-pricing-2026-plans-credits-commercial-rights-api-costs/"),
            ("Trustpilot ElevenLabs reviews", "https://www.trustpilot.com/review/elevenlabs.io"),
            ("Reddit ElevenLabs cost review", "https://www.reddit.com/r/LovedByCreators/comments/1s3zebv/elevenlabs_review_what_it_actually_costs_once/"),
        ],
        "purpose": "ElevenLabs is an AI audio platform for realistic text-to-speech, speech-to-text, voice cloning, dubbing, sound effects, music, and voice agents.",
        "company": "ElevenLabs",
        "users": "creators, publishers, game studios, educators, localization teams, developers, contact centers, and enterprises building voice products",
        "market": "AI voice, speech synthesis, dubbing/localization, voice agents, audio generation, and speech APIs",
        "pricing": "consumer/creator subscriptions and API pricing; API charges are usage-based for speech, dubbing, music, voice isolation, and related services",
        "business": "subscription, usage-based API, enterprise voice deployments, and voice marketplace/licensing",
        "positioning": "high-quality humanlike voice AI and deployable voice agents",
        "philosophy": "spoken AI should sound natural, multilingual, low-latency, and production-ready",
        "vision": "make high-quality voice generation and conversational agents available through tools and APIs",
        "problem": "voice production, dubbing, narration, and voice support are slow, expensive, and hard to scale across languages.",
        "before": "voice actors, studios, call centers, manual dubbing, basic TTS, and audio editing tools.",
        "why": "users choose ElevenLabs for voice quality, cloning, multilingual dubbing, low-latency APIs, and new voice-agent capabilities.",
        "features": "text-to-speech, speech-to-text, voice cloning, voice design, voice changer, voice isolator, dubbing, sound effects, music, studio, API/SDK, low-latency streaming, voice agents, and safety controls",
        "journey": "A user signs up, selects or clones a voice, generates speech or dubbing, edits settings, exports audio, or integrates APIs/agents into an app or support workflow.",
        "ia": "IA includes voice library, studio, projects, dubbing, agents, API keys/docs, usage/pricing, voices, safety, billing, and enterprise controls.",
        "ux": "The UX is strong for fast high-quality audio. Friction appears when users must understand credits/API costs, rights, cloning consent, and production-scale pricing.",
        "ai": "AI includes multilingual speech generation, transcription, voice conversion, cloning, sound/music generation, and voice agents. Safety systems are central because misuse risk is high.",
        "technical": "Hosted model platform plus APIs/SDKs for speech and agents. Exact model training data and architecture are not fully public.",
        "integrations": "API/SDK, voice agents, apps, creative tools, call/chat/email/WhatsApp-style agent channels, and embedding into developer products.",
        "automation": "Automation includes TTS generation, dubbing pipelines, voice agents, transcription, audio cleanup, and API-driven content production.",
        "collaboration": "Team and enterprise workflows support shared projects, voices, and usage controls where available.",
        "customization": "Customization includes voice selection, voice cloning, style settings, languages, pronunciation, API parameters, and agent behavior.",
        "security": "Safety and consent controls are critical due to voice cloning. Enterprises must check verification, abuse prevention, data retention, and commercial rights.",
        "performance": "Known for strong voice quality and low latency; costs can rise quickly for production workloads and voice quality varies by language/use case.",
        "community": "Large creator/developer community, Trustpilot reviews, Reddit cost discussions, YouTube tutorials, and enterprise/audio-industry coverage.",
        "strengths": ["excellent voice quality", "broad audio feature set", "API-first platform", "voice agents direction", "multilingual dubbing"],
        "weaknesses": ["cost can rise quickly", "voice-cloning misuse risk", "pricing complexity", "support complaints in reviews", "rights/consent require care"],
        "missing": ["simpler cost estimator", "stronger built-in rights workflow", "voice provenance dashboards", "team review approvals", "more transparent model controls"],
        "opportunities": ["voice-agent operating system", "localization factory", "licensed voice marketplace", "audio content automation", "compliance-first voice cloning"],
        "rating": ["Ease of Use: 8/10", "Features: 9/10", "Performance: 9/10", "Customization: 9/10", "AI: 10/10", "Automation: 8/10", "Integrations: 9/10", "Scalability: 9/10", "Innovation: 9/10", "Value for Money: 7/10", "Overall: 8.6/10"],
    },
    {
        "path": "reports/ai-coding/github-copilot.md",
        "name": "GitHub Copilot",
        "original": "GitHub Copilot",
        "category": "AI Coding",
        "status": "Research drafted - batch 006",
        "sources": [
            ("GitHub Copilot plans docs", "https://docs.github.com/en/copilot/get-started/plans"),
            ("GitHub Copilot docs", "https://docs.github.com/en/copilot"),
            ("GitHub pricing", "https://github.com/pricing"),
            ("GitHub Copilot usage-based billing announcement", "https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/"),
            ("TechJack GitHub Copilot review", "https://techjacksolutions.com/ai-tools/microsoft-copilot/github-copilot-review/"),
            ("Business Insider Copilot billing reaction", "https://www.businessinsider.com/github-copilot-token-uage-pricing-change-reaction-2026-6"),
            ("ITPro Copilot pricing changes", "https://www.itpro.com/software/development/github-copilot-pricing-changes-usage-based-billing-explained"),
        ],
        "purpose": "GitHub Copilot is GitHub's AI coding assistant for code completion, chat, code review, agentic coding, documentation, tests, security help, and repository-aware development.",
        "company": "GitHub / Microsoft",
        "users": "developers, engineering teams, open-source maintainers, enterprises, students, and platform teams",
        "market": "AI coding assistants, developer productivity, code review automation, and agentic software development",
        "pricing": "Free/Pro/Business/Enterprise tiers with completions and AI credits; GitHub moved Copilot plans toward usage-based AI Credits on June 1, 2026",
        "business": "seat subscriptions plus usage-based AI credits, enterprise platform bundles, and GitHub ecosystem expansion",
        "positioning": "AI pair programmer integrated into GitHub and developer tools",
        "philosophy": "AI should help developers stay in flow while coding, reviewing, testing, and understanding repositories",
        "vision": "make GitHub the AI-powered software development platform from issue to pull request to deployment",
        "problem": "developers spend time on boilerplate, search, tests, code review, debugging, and repository understanding.",
        "before": "manual coding, Stack Overflow, IDE autocomplete, linters, code review, ChatGPT, local scripts, and documentation searches.",
        "why": "users choose Copilot because it is deeply integrated into GitHub/IDEs, works across repository context, and is supported by enterprise controls.",
        "features": "code completions, chat, inline edits, code review, pull request summaries, agent/cloud coding, knowledge bases, model selection, security assistance, enterprise policies, usage/budget controls, and IDE/GitHub integration",
        "journey": "A developer installs Copilot, accepts completions, asks chat for help, uses repository context, requests tests/refactors, opens PRs with summaries/reviews, and teams configure policies/budgets.",
        "ia": "IA spans IDE extension, GitHub UI, PRs, issues, Copilot settings, enterprise admin, usage/billing, model controls, and documentation.",
        "ux": "Copilot is strong because it appears in the developer workflow. The 2026 billing shift adds cost-awareness friction for agentic and advanced model use.",
        "ai": "AI includes completions, chat, edits, code review, repository context, cloud agent, model selection, and security/code understanding. Models vary by plan and feature.",
        "technical": "Hosted AI service integrated with IDEs and GitHub. Enterprise features include policies, knowledge bases, admin controls, and usage budgets. Exact model routing internals are not fully public.",
        "integrations": "GitHub, VS Code, JetBrains, Visual Studio, Xcode-related surfaces where supported, CLI/web, PRs/issues, Actions-adjacent workflows, and enterprise identity/admin.",
        "automation": "Automation includes code generation, refactors, tests, PR summaries, code review, agentic tasks, and security scanning/recommendations.",
        "collaboration": "Strong via GitHub PRs, code review, teams, enterprise settings, knowledge bases, and organization-level policies.",
        "customization": "Customization includes instructions, repository context, knowledge bases, model choice, policies, budget caps, and IDE preferences.",
        "security": "Enterprise controls, policy settings, data-handling options, and code-scanning/security features matter. Generated code still needs human review.",
        "performance": "Excellent for routine coding and repo assistance; costs and outages/capacity concerns are current risks for heavy AI-agent use.",
        "community": "Huge developer adoption, GitHub docs/blogs, Reddit, Hacker News, enterprise reports, and competitive comparisons with Cursor/Claude Code/Codex.",
        "strengths": ["deep GitHub/IDE integration", "mature enterprise controls", "strong completions", "repo-aware workflows", "large ecosystem"],
        "weaknesses": ["usage billing backlash", "AI credits hard to predict", "agentic work can burn budget", "not always architecture-aware", "generated code can be wrong"],
        "missing": ["clear per-task cost preview", "better agent budget guardrails", "architecture policy checks", "transparent model selection guidance", "stronger rollback for agent changes"],
        "opportunities": ["AI software delivery platform", "review-to-fix automation", "secure coding copilots", "organization knowledge graphs", "cost-aware coding agents"],
        "rating": ["Ease of Use: 9/10", "Features: 9/10", "Performance: 8/10", "Customization: 8/10", "AI: 9/10", "Automation: 8/10", "Integrations: 10/10", "Scalability: 9/10", "Innovation: 9/10", "Value for Money: 7/10", "Overall: 8.5/10"],
    },
    {
        "path": "reports/media-generation/runway.md",
        "name": "Runway",
        "original": "Rumway",
        "category": "Media Generation",
        "status": "Research drafted - batch 006",
        "sources": [
            ("Runway official site", "https://runwayml.com/"),
            ("Runway pricing", "https://runwayml.com/pricing"),
            ("Runway API docs", "https://docs.dev.runwayml.com/"),
            ("Runway API pricing", "https://docs.dev.runwayml.com/guides/pricing/"),
            ("SaaS CRM Runway pricing", "https://saascrmreview.com/runway-ml-pricing/"),
            ("CheckThat Runway pricing", "https://checkthat.ai/brands/runway/pricing"),
            ("AI Tools DevPro Runway Gen-4 guide", "https://aitoolsdevpro.com/ai-tools/runway-guide/"),
        ],
        "purpose": "Runway is an AI creative suite for generating and editing video, images, audio, lip sync, motion, and cinematic production assets.",
        "company": "Runway",
        "users": "filmmakers, marketers, creators, agencies, studios, social media teams, and developers building video-generation workflows",
        "market": "AI video generation, creative production, generative media APIs, and video editing",
        "pricing": "free, Standard, Pro, Max, and Enterprise-style plans with credit-based image/video generation plus API credits",
        "business": "subscription, credit usage, enterprise creative production, and developer API monetization",
        "positioning": "professional AI video and creative generation platform",
        "philosophy": "AI should give creators new cinematic tools while staying inside an editor-like production workflow",
        "vision": "a generative media studio for creators and teams, from prompt to production asset",
        "problem": "video production is slow, expensive, and requires specialized skills, equipment, editing, and iteration.",
        "before": "camera shoots, stock video, After Effects/Premiere, freelancers, animation tools, and manual VFX workflows.",
        "why": "users choose Runway for advanced video models, editing tools, API access, creative controls, and professional production orientation.",
        "features": "text-to-video, image-to-video, Gen models, image generation, upscaling, lip sync, text-to-speech/custom voices, asset storage, teamspaces, API, credits, enterprise analytics, and priority support",
        "journey": "A creator uploads or prompts a scene, generates clips, refines with controls, upscales or extends, edits into a sequence, exports, or calls the API for programmatic generation.",
        "ia": "IA includes projects/assets, generation tools, model picker, timeline/editor, storage, credits, API/developer portal, teams, billing, and enterprise admin.",
        "ux": "Runway is strong for creative exploration. Friction comes from credit math, unpredictable generations, render wait times, and needing many attempts for production-quality shots.",
        "ai": "AI includes video/image generation, multimodal generation, audio/voice tools, upscaling, and model-specific controls. Exact model internals are not public.",
        "technical": "Hosted GPU-heavy media generation platform with web app and API. API credits can be purchased for organizations and consumed by model/task type.",
        "integrations": "API, asset exports, creative workflows, enterprise teamspaces, and downstream video-editing tools through exports.",
        "automation": "Automation includes prompt-to-video, API generation, batch creative workflows, upscaling, lip sync, and media pipeline integration.",
        "collaboration": "Teamspaces, configurable enterprise team setup, asset storage, workspace analytics, and onboarding/support on enterprise plans.",
        "customization": "Customization includes prompts, references, model choices, output resolution/duration, voices, storage, team settings, and API workflows.",
        "security": "Enterprise features include SSO and team controls; media rights, training/data terms, and asset privacy should be reviewed by plan.",
        "performance": "Strong frontier video capability, but generation cost/time and consistency are the core production constraints.",
        "community": "Strong creator/filmmaker community, YouTube tutorials, pricing guides, developer/API coverage, and AI video comparisons.",
        "strengths": ["leading AI video focus", "professional creative workflow", "API access", "team/enterprise options", "broad media tools"],
        "weaknesses": ["credit costs can surprise users", "generation consistency is hard", "longer clips require many attempts", "commercial production still needs editing", "model limits change quickly"],
        "missing": ["shot-level consistency tools", "clear cost estimate before generation", "stronger storyboard workflow", "rights/provenance dashboard", "native production review system"],
        "opportunities": ["AI previsualization platform", "brand video generator", "creative API infrastructure", "storyboard-to-video workflow", "enterprise media automation"],
        "rating": ["Ease of Use: 8/10", "Features: 9/10", "Performance: 8/10", "Customization: 8/10", "AI: 9/10", "Automation: 8/10", "Integrations: 7/10", "Scalability: 8/10", "Innovation: 9/10", "Value for Money: 7/10", "Overall: 8.1/10"],
    },
    {
        "path": "reports/media-generation/midjourney.md",
        "name": "Midjourney",
        "original": "Midjourney",
        "category": "Media Generation",
        "status": "Research drafted - batch 006",
        "sources": [
            ("Midjourney docs", "https://docs.midjourney.com/hc/en-us"),
            ("Midjourney plan comparison", "https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans"),
            ("Midjourney version docs", "https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version"),
            ("Midjourney V8.1 update", "https://updates.midjourney.com/v8-1-alpha/"),
            ("Midjourney terms", "https://docs.midjourney.com/hc/en-us/articles/32083055291277-Terms-of-Service"),
            ("Product Hunt Midjourney reviews", "https://www.producthunt.com/products/midjourney/reviews"),
            ("Trustpilot Midjourney reviews", "https://www.trustpilot.com/review/www.midjourney.com"),
            ("Reddit Midjourney restrictions discussion", "https://www.reddit.com/r/midjourney/comments/1r4g4sw/midjourney_is_gonna_die_unless_they_fix_this/"),
        ],
        "purpose": "Midjourney is an AI image and visual generation platform known for high-quality artistic outputs, prompt-based image creation, web/Discord workflows, personalization, and emerging video tools.",
        "company": "Midjourney",
        "users": "artists, designers, creators, marketers, concept artists, agencies, game teams, and visual experimenters",
        "market": "AI image generation, concept art, creative ideation, marketing visuals, and generative media",
        "pricing": "Basic, Standard, Pro, and Mega subscriptions with monthly/yearly billing, GPU/relax-mode limits, and Stealth Mode on higher tiers",
        "business": "subscription-based access to generative media models and compute",
        "positioning": "imaginative visual generation with a distinctive high-quality aesthetic",
        "philosophy": "AI can expand human imagination by making visual exploration fast, beautiful, and iterative",
        "vision": "new mediums of thought and expanded imaginative powers through generative visuals",
        "problem": "high-quality visual ideation traditionally requires artists, time, stock libraries, moodboards, or expensive concept development.",
        "before": "stock images, Photoshop, illustrators, Pinterest/moodboards, 3D tools, and manual concept art.",
        "why": "users choose Midjourney for aesthetic quality, fast ideation, personalization, community inspiration, and strong image-generation output.",
        "features": "text-to-image, image prompts, style/reference controls, personalization profiles, web app, Discord access, V8/V8.1 models, Raw mode, faster rendering, HD output, video/image-to-video tools, Stealth Mode, and galleries/community",
        "journey": "A user signs in via web or Discord, picks a plan, writes prompts or image references, generates grids, upscales/varies/remixes, saves images, shares or keeps private depending on plan, and iterates styles over time.",
        "ia": "IA includes web gallery, create prompt field, image history, explore/community, model/version settings, style/personalization controls, billing, documentation, and Discord channels.",
        "ux": "Midjourney is magical for visual exploration but weaker for precise production control. Users complain about moderation restrictions, billing/support, prompt adherence, and exact design requirements.",
        "ai": "AI includes image generation, prompt interpretation, style/personalization, image references, Raw mode, and newer video/image-to-video capabilities. Exact model training details are not public.",
        "technical": "Hosted generative model platform accessed through web/Discord. Official docs do not provide a mainstream public developer API; third-party API wrappers exist but are not official.",
        "integrations": "Official access is web and Discord. External integration is limited compared with API-first tools.",
        "automation": "Automation is mostly manual prompting and iteration; lack of official API limits production automation.",
        "collaboration": "Community and galleries are strong. Team/enterprise collaboration and private client workflows depend heavily on plan/privacy options.",
        "customization": "Customization includes prompts, image/style references, model versions, Raw mode, personalization profiles, aspect ratios, and privacy/Stealth Mode on higher plans.",
        "security": "Users should review terms, privacy, public gallery behavior, Stealth Mode, rights, and client confidentiality before professional use.",
        "performance": "V8.1 is documented as faster and better at prompt details. Performance still depends on GPU mode, prompt complexity, and iteration volume.",
        "community": "Huge creative community across Discord, Reddit, YouTube, Product Hunt, galleries, and prompt-sharing ecosystems.",
        "strengths": ["exceptional aesthetic quality", "fast ideation", "strong community", "personalization/style controls", "mature web/Discord workflows"],
        "weaknesses": ["limited official API", "moderation restrictions frustrate users", "precise text/control remains hard", "billing/support complaints", "private work requires higher tiers"],
        "missing": ["official public API", "better typography/control", "enterprise review workflow", "clearer cost/GPU forecasting", "more transparent moderation explanations"],
        "opportunities": ["professional concept-art pipeline", "brand-controlled visual generation", "official API ecosystem", "creative collaboration boards", "rights/provenance management"],
        "rating": ["Ease of Use: 8/10", "Features: 8/10", "Performance: 9/10", "Customization: 8/10", "AI: 9/10", "Automation: 5/10", "Integrations: 5/10", "Scalability: 7/10", "Innovation: 9/10", "Value for Money: 8/10", "Overall: 7.8/10"],
    },
]


def source_log(r):
    return "\n".join(f"- [{label}]({url})" for label, url in r["sources"])


def feature_sections(r):
    out = []
    for category in FEATURE_CATEGORIES:
        desc = r["features"] if category == "Core Features" else f"{category} are available where documented, with depth depending on plan, product surface, and current release."
        if category == "Offline Features":
            desc = "Offline support is limited or not central; generation generally depends on hosted models and cloud compute."
        out.append(f"### {category}\n- Description: {desc}\n- Why it exists: To make AI generation useful in repeatable production workflows.\n- User benefit: Users can create, iterate, automate, and govern creative or coding work faster.\n")
    return "\n".join(out)


def bullets(items):
    return "\n".join(f"- {x}" for x in items)


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
- Why does this problem exist? High-quality creative or engineering output requires specialized skill, iteration, compute, tooling, and review.
- How did people solve this before? {r['before']}
- Why do users choose this product? {r['why']}

## 3. Core Features

{feature_sections(r)}

## 4. Complete User Journey

{r['journey']}

Major interactions include signup, prompt/input setup, generation, review, iteration, export, billing/credits, advanced settings, and team or API use where available.

## 5. Information Architecture

{r['ia']}

The IA should keep creation, history, assets, settings, billing, safety/privacy, and exports easy to find.

## 6. UX Analysis

{r['ux']}

The best UX makes generation feel creative and controlled. The weakest UX hides cost, moderation, model limits, or rights issues.

## 7. AI Features

{r['ai']}

AI should be evaluated for quality, consistency, controllability, model/version transparency, safety, and production repeatability.

## 8. Technical Analysis

{r['technical']}

Unknowns include exact model architecture, training data, inference stack, queueing, moderation systems, and internal evaluation unless disclosed.

## 9. Integrations

{r['integrations']}

Integration value depends on API access, app embedding, export paths, identity/admin controls, and workflow compatibility.

## 10. Automation

{r['automation']}

Automation should expose costs, retries, failed generations, permissions, and asset provenance.

## 11. Collaboration

{r['collaboration']}

Collaboration matters for agencies, studios, enterprises, and engineering teams where review, privacy, and role boundaries affect adoption.

## 12. Customization

{r['customization']}

Customization is valuable when it improves consistency without making the workflow too complex.

## 13. Security

{r['security']}

Security review should include privacy, intellectual property, generated-output rights, model/data policies, SSO/admin, and abuse controls.

## 14. Performance

{r['performance']}

Performance should be judged by usable output per dollar/minute, not raw generation speed alone.

## 15. Community

{r['community']}

Community signals reveal real quality, pricing, support, and moderation issues that official pages tend to smooth over.

## 16. Strengths

{bullets(r['strengths'])}

## 17. Weaknesses

{bullets(r['weaknesses'])}

## 18. Missing Features

{bullets(r['missing'])}

These matter because creative and coding users need reliable, repeatable outputs rather than one-off demos.

## 19. Hidden Opportunities

{bullets(r['opportunities'])}

## 20. Reverse Engineering

- Keep: {r['purpose']}
- Redesign: make cost, rights, version, and quality controls more legible.
- Remove: opaque credit burn, unclear permissions, and hidden model constraints.
- Simplify: onboarding, generation settings, export, and production review.

## 21. Competitive Advantages

- Why users stay: asset history, model quality, workflow integration, habit, team setup, and output style.
- What creates lock-in: credits, project libraries, generated assets, team workflows, prompts, voices, or code context.
- Why competitors struggle: they must match quality, speed, trust, and workflow fit simultaneously.

## 22. Ideal User

- Who should use it: {r['users']}.
- Who should avoid it: users who need guaranteed exact outputs, unclear rights tolerance, or zero-review automation.

## 23. SWOT Analysis

- Strengths: {', '.join(r['strengths'][:3])}.
- Weaknesses: {', '.join(r['weaknesses'][:3])}.
- Opportunities: {', '.join(r['opportunities'][:3])}.
- Threats: fast model commoditization, IP litigation, pricing pressure, open-source alternatives, and platform bundling.

## 24. Product Rating

{bullets(r['rating'])}

## 25. Lessons Learned

- Best ideas worth keeping: high-quality generation, workflow embedding, team/API paths, and clear production use cases.
- Worst ideas to avoid: hidden costs, weak rights clarity, moderation surprises, and outputs that cannot be reproduced.
- Innovations worth adapting: AI generation becomes much stronger when paired with editing, governance, and asset workflows.
- Design principles: show cost, provenance, controls, and version clearly.
- Architecture principles: make generation observable, configurable, and safely bounded.
- Business lessons: credits monetize compute but can erode trust if users cannot predict them.
- Product strategy lessons: durable value comes from production workflow fit, not novelty alone.
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
        "| Stable Diffusion | Open-source image generation | Appeared in Firefly and Midjourney competitive context | Adobe Firefly; Midjourney | https://stability.ai/ | Important open model ecosystem for image generation. |",
        "| Adobe Express | Creative platform | Appeared in Firefly integration research | Adobe Firefly | https://www.adobe.com/express/ | Useful lightweight creative workflow adjacent to Firefly. |",
        "| Murf AI | AI voice | Appeared in ElevenLabs competitive context | ElevenLabs | https://murf.ai/ | Voice generation competitor to consider. |",
        "| Cursor | AI coding IDE | Appeared in Copilot competitive context | GitHub Copilot | https://cursor.com/ | Already on main list, but reinforced as high-priority AI coding comparison. |",
        "| Luma AI | AI video | Appeared in Runway/Midjourney competitive context | Runway; Midjourney | https://lumalabs.ai/ | Candidate video-generation competitor. |",
        "| Kling AI | AI video | Appeared in Runway pricing/model context | Runway | https://klingai.com/ | Already on main list, but relevant to video generation comparisons. |",
    ]
    for line in additions:
        if line not in ctext:
            ctext += "\n" + line
    candidates.write_text(ctext.rstrip() + "\n", encoding="utf-8")
    print("Batch 006 reports filled: Adobe Firefly, ElevenLabs, GitHub Copilot, Runway, Midjourney")


if __name__ == "__main__":
    main()
