---
layout: default
title: Beyond Blind Spots: Analytic Hints for Mitigating LLM-Based Evaluation Pitfalls
---

# Beyond Blind Spots: Analytic Hints for Mitigating LLM-Based Evaluation Pitfalls

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16272" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16272v1</a>
  <a href="https://arxiv.org/pdf/2512.16272.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16272v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16272v1', 'Beyond Blind Spots: Analytic Hints for Mitigating LLM-Based Evaluation Pitfalls')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ora Nova Fandina, Eitan Farchi, Shmulik Froimovich, Raviv Gal, Wesam Ibraheem, Rami Katan, Alice Podolsky

**分类**: cs.SE, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**利用分析提示缓解LLM在代码评估中的盲点，提升COBOL代码生成质量**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `代码评估` `领域知识` `分析提示` `COBOL代码`

## 📋 核心要点

1. 现有LaaJ在代码生成评估中存在领域知识盲点，导致关键错误被忽略，影响评估可靠性。
2. 提出一种分析提示方法，通过轻量级分析检查工具识别领域特定问题，并将其作为提示注入LaaJ。
3. 实验表明，LaaJ+提示配置显著提升错误检测覆盖率（最高达94%），并生成更准确的解释。

## 📝 摘要（中文）

大型语言模型（LLM）越来越多地被部署为代码生成流程中的评估者（LaaJ）。尽管这种方式具有可扩展性，但LaaJ往往会忽略特定领域的关键问题，引发对其在关键评估任务中可靠性的担忧。为了更好地理解这些局限性，本文在一个具体的工业用例中检验了LaaJ的行为：通过COBOL代码生成实现遗留代码现代化。研究发现，即使是生产环境中部署的LaaJ也可能遗漏领域关键错误，暴露出其评估能力中存在的盲点。为了更好地理解这些盲点，本文分析了生成的COBOL程序和相关的LaaJ判断，并利用专家知识构建了一个初步的分类体系。基于此，开发了一个轻量级的分析检查工具，可以标记实践中观察到的30多个特定领域问题。该工具的输出被用作分析提示，动态地注入到评估者的提示中，以鼓励LaaJ重新审视可能被忽略的方面。在包含100个程序的测试集上，使用四个生产级别的LaaJ进行的实验表明，LaaJ单独只能检测到代码中约45%的错误，而分析检查器本身缺乏解释深度。当结合使用时，LaaJ+提示配置实现了高达94%的覆盖率，并产生了质量更高、更准确的解释，证明了分析-LLM混合方法可以显著提高已部署流程中的评估可靠性。本文发布了数据集和所有使用的提示。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在作为代码生成评估者（LaaJ）时，由于缺乏特定领域的知识而导致的评估盲点问题。现有方法依赖于LLM自身的理解能力，容易忽略COBOL等遗留代码中的领域特定错误，从而影响代码质量和可靠性。

**核心思路**：论文的核心思路是将领域专家知识融入到LLM的评估过程中。通过构建一个轻量级的分析检查工具，该工具能够识别COBOL代码中常见的领域特定问题，并将这些问题作为“分析提示”注入到LLM的评估提示中。这样，LLM在评估代码时，可以借助这些提示来关注可能被忽略的关键方面，从而提高评估的准确性和可靠性。

**技术框架**：该方法的技术框架主要包含以下几个模块：1) COBOL代码生成器：生成需要评估的COBOL代码。2) 分析检查工具：基于领域专家知识，对生成的COBOL代码进行静态分析，识别潜在的领域特定问题。3) 提示注入模块：将分析检查工具的输出（即分析提示）动态地注入到LLM的评估提示中。4) LLM评估器（LaaJ）：使用带有分析提示的提示，对生成的COBOL代码进行评估，并给出评估结果和解释。

**关键创新**：该方法最重要的技术创新点在于将领域专家知识与LLM的评估能力相结合。通过分析提示，弥补了LLM在特定领域知识方面的不足，使其能够更准确地识别代码中的错误。这种混合方法不仅提高了评估的准确性，还增强了评估结果的可解释性。

**关键设计**：分析检查工具的设计是关键。它需要能够覆盖COBOL代码中常见的领域特定问题，例如数据类型转换、变量初始化、错误处理等。提示注入模块的设计也需要考虑如何将分析提示有效地融入到LLM的评估提示中，以最大程度地发挥提示的作用。论文中使用了超过30种领域特定问题的检查规则，并探索了不同的提示注入方式，以找到最佳的配置。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16272v1/hint_llaj.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16272v1/taxonomy.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16272v1/hybrid_laaj_issues_triplets_total_native_orange_leftlegend.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，单独使用LaaJ只能检测到约45%的错误，而结合分析提示后，错误检测覆盖率最高可达94%。此外，LaaJ+提示配置生成的评估解释也更加准确和丰富。这些结果表明，分析-LLM混合方法可以显著提高代码评估的可靠性。

## 🎯 应用场景

该研究成果可应用于遗留系统现代化改造、代码质量评估、自动化代码审查等领域。通过提升LLM在特定领域代码评估中的准确性和可靠性，可以降低人工成本，提高开发效率，并减少潜在的软件缺陷。该方法具有通用性，可以扩展到其他领域，例如金融、医疗等，具有广阔的应用前景。

## 📄 摘要（原文）

> Large Language Models are increasingly deployed as judges (LaaJ) in code generation pipelines. While attractive for scalability, LaaJs tend to overlook domain specific issues raising concerns about their reliability in critical evaluation tasks. To better understand these limitations in practice, we examine LaaJ behavior in a concrete industrial use case: legacy code modernization via COBOL code generation. In this setting, we find that even production deployed LaaJs can miss domain critical errors, revealing consistent blind spots in their evaluation capabilities.
>   To better understand these blind spots, we analyze generated COBOL programs and associated LaaJs judgments, drawing on expert knowledge to construct a preliminary taxonomy. Based on this taxonomy, we develop a lightweight analytic checker tool that flags over 30 domain specific issues observed in practice. We use its outputs as analytic hints, dynamically injecting them into the judges prompt to encourage LaaJ to revisit aspects it may have overlooked.
>   Experiments on a test set of 100 programs using four production level LaaJs show that LaaJ alone detects only about 45% of the errors present in the code (in all judges we tested), while the analytic checker alone lacks explanatory depth. When combined, the LaaJ+Hints configuration achieves up to 94% coverage (for the best performing judge and injection prompt) and produces qualitatively richer, more accurate explanations, demonstrating that analytic-LLM hybrids can substantially enhance evaluation reliability in deployed pipelines. We release the dataset and all used prompts.

