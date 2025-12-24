---
layout: default
title: "Beyond Blind Spots: Analytic Hints for Mitigating LLM-Based Evaluation Pitfalls"
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

**利用分析提示缓解LLM代码评估中的盲点，提升COBOL代码生成质量**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `代码评估` `领域知识` `分析提示` `COBOL代码生成`

## 📋 核心要点

1. 现有LaaJ在代码生成评估中存在领域盲点，无法有效识别特定领域的关键错误，影响评估可靠性。
2. 提出一种分析提示方法，通过轻量级分析检查工具识别领域特定问题，并将其作为提示注入LaaJ，引导其重新评估。
3. 实验表明，LaaJ+提示配置显著提升错误检测覆盖率，最高可达94%，并生成更准确的解释，验证了混合方法的有效性。

## 📝 摘要（中文）

大型语言模型（LLM）越来越多地被部署为代码生成流程中的评估者（LaaJ）。尽管这种方式具有可扩展性，但LaaJ容易忽略特定领域的细节问题，引发了对其在关键评估任务中可靠性的担忧。为了更好地理解这些局限性，本文研究了LaaJ在工业用例中的表现：通过COBOL代码生成实现遗留代码现代化。研究发现，即使是生产环境中部署的LaaJ也会遗漏领域关键错误，揭示了其评估能力中存在的盲点。为了更好地理解这些盲点，本文分析了生成的COBOL程序和LaaJ的判断，并利用专家知识构建了一个初步的分类体系。基于此，开发了一个轻量级的分析检查工具，可以标记实践中观察到的30多个特定领域的问题。该工具的输出被用作分析提示，动态地注入到评估者的提示中，以鼓励LaaJ重新审视可能被忽略的方面。在包含100个程序的测试集上，使用四个生产级别的LaaJ进行的实验表明，LaaJ单独检测到的错误仅占代码中存在的错误的45%左右（在所有测试的评估者中），而分析检查器本身缺乏解释深度。当结合使用时，LaaJ+提示配置实现了高达94%的覆盖率（对于性能最佳的评估者和注入提示），并产生了质量更高、更准确的解释，证明了分析-LLM混合方法可以显著提高已部署流程中的评估可靠性。本文发布了数据集和所有使用的提示。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在作为代码生成评估者（LaaJ）时，由于缺乏特定领域知识而产生的评估盲点问题。现有方法依赖于LLM自身的泛化能力，容易忽略COBOL等遗留代码现代化过程中的关键错误，导致评估结果不准确，影响代码质量。

**核心思路**：论文的核心思路是将领域专家的知识融入到LLM的评估过程中。通过构建一个轻量级的分析检查工具，该工具能够识别COBOL代码中常见的特定领域问题，并将这些问题以“提示”的形式反馈给LLM，引导LLM重新审视代码中可能存在的错误。这种方法结合了LLM的泛化能力和领域专家的专业知识，从而提高评估的准确性和可靠性。

**技术框架**：该方法主要包含以下几个阶段：
1. **COBOL代码生成**：使用代码生成模型生成COBOL代码。
2. **分析检查**：使用轻量级分析检查工具对生成的COBOL代码进行静态分析，识别潜在的领域特定问题。
3. **提示注入**：将分析检查工具的输出作为“提示”注入到LLM的评估提示中。
4. **LLM评估**：LLM基于带有提示的输入，对生成的COBOL代码进行评估，并给出评估结果和解释。
5. **结果分析**：分析LLM的评估结果，评估该方法在提高评估准确性方面的效果。

**关键创新**：该方法最重要的创新点在于将领域专家的知识以“提示”的形式动态地注入到LLM的评估过程中。与传统的LLM评估方法相比，该方法能够有效地缓解LLM在特定领域知识方面的不足，从而提高评估的准确性和可靠性。此外，轻量级分析检查工具的设计也降低了计算成本，使其更易于部署和应用。

**关键设计**：分析检查工具的设计是关键。它需要能够准确识别COBOL代码中常见的特定领域问题，例如数据类型不匹配、变量未初始化、循环边界错误等。提示注入的方式也需要仔细设计，以确保LLM能够有效地利用这些提示信息。论文中使用了多种提示模板，并通过实验选择最佳的提示模板。此外，论文还对不同的LLM进行了实验，以评估该方法在不同LLM上的效果。

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

实验结果表明，单独使用LaaJ只能检测到约45%的错误，而结合分析提示后，错误检测覆盖率最高可达94%。这表明分析提示能够显著提升LLM在代码评估中的性能。此外，LaaJ+提示配置还能生成质量更高、更准确的解释，有助于开发人员更好地理解和修复代码中的问题。

## 🎯 应用场景

该研究成果可应用于遗留代码现代化、代码质量评估、自动化代码审查等领域。通过结合领域知识和LLM的推理能力，可以显著提高代码评估的准确性和效率，降低软件开发和维护成本。未来，该方法可以扩展到其他编程语言和领域，为软件工程的自动化和智能化提供更强大的支持。

## 📄 摘要（原文）

> Large Language Models are increasingly deployed as judges (LaaJ) in code generation pipelines. While attractive for scalability, LaaJs tend to overlook domain specific issues raising concerns about their reliability in critical evaluation tasks. To better understand these limitations in practice, we examine LaaJ behavior in a concrete industrial use case: legacy code modernization via COBOL code generation. In this setting, we find that even production deployed LaaJs can miss domain critical errors, revealing consistent blind spots in their evaluation capabilities.
>   To better understand these blind spots, we analyze generated COBOL programs and associated LaaJs judgments, drawing on expert knowledge to construct a preliminary taxonomy. Based on this taxonomy, we develop a lightweight analytic checker tool that flags over 30 domain specific issues observed in practice. We use its outputs as analytic hints, dynamically injecting them into the judges prompt to encourage LaaJ to revisit aspects it may have overlooked.
>   Experiments on a test set of 100 programs using four production level LaaJs show that LaaJ alone detects only about 45% of the errors present in the code (in all judges we tested), while the analytic checker alone lacks explanatory depth. When combined, the LaaJ+Hints configuration achieves up to 94% coverage (for the best performing judge and injection prompt) and produces qualitatively richer, more accurate explanations, demonstrating that analytic-LLM hybrids can substantially enhance evaluation reliability in deployed pipelines. We release the dataset and all used prompts.

