---
layout: default
title: "SecureFixAgent: A Hybrid LLM Agent for Automated Python Static Vulnerability Repair"
---

# SecureFixAgent: A Hybrid LLM Agent for Automated Python Static Vulnerability Repair

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16275" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16275v1</a>
  <a href="https://arxiv.org/pdf/2509.16275.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16275v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16275v1', 'SecureFixAgent: A Hybrid LLM Agent for Automated Python Static Vulnerability Repair')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jugal Gajjar, Kamalasankari Subramaniakuppusamy, Relsy Puthal, Kaustik Ranaware

**分类**: cs.CR, cs.AI, cs.SE

**发布日期**: 2025-09-18

**备注**: 6 pages, 3 figures, 4 tables, 1 algorithm, accepted in the Robustness and Security of Large Language Models (ROSE-LLM) special session at ICMLA 2025

---

## 💡 一句话要点

**SecureFixAgent：一种混合LLM Agent，用于自动化Python静态漏洞修复。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `漏洞修复` `静态分析` `大型语言模型` `混合框架` `自动化修复`

## 📋 核心要点

1. 现有静态分析工具如Bandit误报率高且缺乏修复能力，而大型语言模型虽能提供修复建议，但易产生幻觉性修改且缺乏验证。
2. SecureFixAgent采用混合框架，结合Bandit的检测能力和轻量级LLM的修复能力，通过迭代的检测-修复-验证循环实现自动化漏洞修复。
3. 实验结果表明，SecureFixAgent有效降低了误报率，提高了修复准确率，并获得了开发人员对解释质量的高度评价。

## 📝 摘要（中文）

现代软件开发流程在保护具有广泛依赖关系的大型代码库方面面临日益严峻的挑战。静态分析工具（如Bandit）在漏洞检测方面有效，但存在高误报率和缺乏修复能力的问题。相比之下，大型语言模型（LLM）可以提出修复建议，但经常产生幻觉性修改，并且缺乏自我验证。我们提出了SecureFixAgent，一个混合修复框架，它将Bandit与轻量级本地LLM（<8B参数）集成在一个迭代的检测-修复-验证循环中。为了提高精度，我们对一个多样化的、经过整理的数据集进行了基于LoRA的参数高效微调，该数据集跨越多个Python项目领域，从而减轻了数据集偏差并减少了不必要的编辑。SecureFixAgent使用Bandit进行检测，LLM用于提供带有解释的候选修复，并使用Bandit重新验证进行验证，所有这些都在本地执行，以保护隐私并减少对云的依赖。实验表明，SecureFixAgent比静态分析降低了10.8%的误报率，提高了13.51%的修复准确率，并且比预训练的LLM降低了5.46%的误报率，通常在三次迭代内收敛。除了指标之外，开发人员研究对解释质量的评分为4.5/5，突出了其对人类信任和采用的价值。通过在资源高效的本地框架中结合可验证的安全改进和透明的原理，SecureFixAgent推进了现代流程中可信赖的自动化漏洞修复。

## 🔬 方法详解

**问题定义**：论文旨在解决Python代码中静态漏洞的自动修复问题。现有静态分析工具（如Bandit）虽然能检测漏洞，但误报率高，且无法提供修复建议。而直接使用大型语言模型进行修复，又容易产生不准确或不安全的修改，缺乏可信度。

**核心思路**：论文的核心思路是结合静态分析工具和大型语言模型的优点，构建一个混合修复框架。利用静态分析工具进行精确的漏洞检测，然后利用大型语言模型生成修复建议，最后再利用静态分析工具进行验证，形成一个迭代的修复循环。

**技术框架**：SecureFixAgent框架包含三个主要模块：漏洞检测模块（使用Bandit），修复建议生成模块（使用轻量级LLM），以及验证模块（使用Bandit重新验证）。整个流程如下：首先，Bandit检测代码中的漏洞；然后，LLM根据漏洞信息生成修复建议，并给出解释；最后，Bandit重新验证修复后的代码，如果漏洞仍然存在，则重复修复过程，直到漏洞被修复或达到最大迭代次数。

**关键创新**：该论文的关键创新在于混合框架的设计，它将静态分析工具的精确性和大型语言模型的生成能力结合起来，实现了更准确、更可信的自动化漏洞修复。此外，使用LoRA进行参数高效微调，降低了计算成本，并缓解了数据集偏差。

**关键设计**：论文使用参数量小于8B的轻量级LLM，并采用LoRA进行微调，以降低计算资源需求。微调数据集涵盖多个Python项目领域，以提高模型的泛化能力。修复建议生成模块会为每个修复建议提供解释，以提高可信度。迭代修复循环的最大迭代次数是一个重要的参数，需要根据实际情况进行调整。

## 📊 实验亮点

实验结果表明，SecureFixAgent相比于单独使用静态分析工具，误报率降低了10.8%，修复准确率提高了13.51%。与预训练的LLM相比，误报率降低了5.46%。开发人员对SecureFixAgent生成的修复建议的解释质量给出了4.5/5的评分，表明其具有良好的可解释性和可信度。

## 🎯 应用场景

SecureFixAgent可应用于软件开发生命周期的各个阶段，例如代码审查、持续集成和持续部署等。它可以帮助开发人员快速发现和修复代码中的安全漏洞，提高软件的安全性，降低安全风险。该研究成果对于构建更安全、更可靠的软件系统具有重要意义。

## 📄 摘要（原文）

> Modern software development pipelines face growing challenges in securing large codebases with extensive dependencies. Static analysis tools like Bandit are effective at vulnerability detection but suffer from high false positives and lack repair capabilities. Large Language Models (LLMs), in contrast, can suggest fixes but often hallucinate changes and lack self-validation. We present SecureFixAgent, a hybrid repair framework integrating Bandit with lightweight local LLMs (<8B parameters) in an iterative detect-repair-validate loop. To improve precision, we apply parameter-efficient LoRA-based fine-tuning on a diverse, curated dataset spanning multiple Python project domains, mitigating dataset bias and reducing unnecessary edits. SecureFixAgent uses Bandit for detection, the LLM for candidate fixes with explanations, and Bandit re-validation for verification, all executed locally to preserve privacy and reduce cloud reliance. Experiments show SecureFixAgent reduces false positives by 10.8% over static analysis, improves fix accuracy by 13.51%, and lowers false positives by 5.46% compared to pre-trained LLMs, typically converging within three iterations. Beyond metrics, developer studies rate explanation quality 4.5/5, highlighting its value for human trust and adoption. By combining verifiable security improvements with transparent rationale in a resource-efficient local framework, SecureFixAgent advances trustworthy, automated vulnerability remediation for modern pipelines.

