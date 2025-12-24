---
layout: default
title: "AutoPK: Leveraging LLMs and a Hybrid Similarity Metric for Advanced Retrieval of Pharmacokinetic Data from Complex Tables and Documents"
---

# AutoPK: Leveraging LLMs and a Hybrid Similarity Metric for Advanced Retrieval of Pharmacokinetic Data from Complex Tables and Documents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00039" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00039v1</a>
  <a href="https://arxiv.org/pdf/2510.00039.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00039v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00039v1', 'AutoPK: Leveraging LLMs and a Hybrid Similarity Metric for Advanced Retrieval of Pharmacokinetic Data from Complex Tables and Documents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hossein Sholehrasa, Amirhossein Ghanaatian, Doina Caragea, Lisa A. Tell, Jim E. Riviere, Majid Jaberi-Douraki

**分类**: cs.DB, cs.AI, cs.IR

**发布日期**: 2025-09-26

**备注**: Accepted at the 2025 IEEE 37th ICTAI

**🔗 代码/项目**: [GITHUB](https://github.com/hosseinsholehrasa/AutoPK)

---

## 💡 一句话要点

**AutoPK：利用LLM和混合相似度量从复杂表格和文档中高效检索药代动力学数据**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `药代动力学` `大型语言模型` `信息抽取` `表格理解` `混合相似度量` `药物研发` `自动化`

## 📋 核心要点

1. 现有PK数据提取方法难以处理表格结构异构和术语不一致的问题，限制了自动化程度。
2. AutoPK采用两阶段框架，结合LLM、混合相似度量和LLM验证，实现准确的PK参数提取。
3. 实验表明，AutoPK显著提升了PK数据提取的精确率和召回率，尤其是在小模型上提升明显。

## 📝 摘要（中文）

药代动力学(PK)在药物开发和人类及兽医药物的监管决策中起着关键作用，通过药物安全性和有效性评估直接影响公众健康。然而，PK数据通常嵌入在具有可变结构和不一致术语的复杂、异构表格中，这给自动PK数据检索和标准化带来了重大挑战。AutoPK是一个新颖的两阶段框架，用于从复杂科学表格中准确且可扩展地提取PK数据。在第一阶段，AutoPK使用大型语言模型(LLM)、混合相似度量和基于LLM的验证来识别和提取PK参数变体。第二阶段过滤相关行，将表格转换为键值文本格式，并使用LLM重建标准化表格。在包含标题和脚注的605个PK表格的真实数据集上进行评估，AutoPK在精确率和召回率方面显示出比直接LLM基线显著的改进。例如，AutoPK与LLaMA 3.1-70B在半衰期参数上实现了0.92的F1分数，在清除率参数上实现了0.91的F1分数，分别优于直接使用LLaMA 3.1-70B的0.10和0.21。

## 🔬 方法详解

**问题定义**：论文旨在解决从复杂科学表格中自动提取药代动力学(PK)数据的难题。现有方法难以应对表格结构的多样性、术语的不一致性以及数据嵌入的复杂性，导致提取精度低、效率低下，阻碍了药物开发和监管决策。

**核心思路**：AutoPK的核心思路是利用大型语言模型(LLM)的强大语义理解能力，结合混合相似度量和LLM验证，分阶段地从复杂表格中提取和标准化PK数据。通过分解任务，降低了对单一模型的依赖，提高了整体的鲁棒性和准确性。

**技术框架**：AutoPK框架包含两个主要阶段：
1. **PK参数变体识别与提取**：利用LLM识别表格中PK参数的各种表达形式，并结合混合相似度量（例如，字符串相似度和语义相似度）进行匹配。使用LLM进行验证，过滤掉不相关的提取结果。
2. **表格标准化与重建**：过滤表格中的相关行，将表格转换为键值对文本格式，然后使用LLM将提取的数据重建为标准化的表格。

**关键创新**：AutoPK的关键创新在于其混合方法，它巧妙地结合了LLM的语义理解能力和传统相似度量方法的精确性。此外，两阶段框架的设计降低了对单一LLM的依赖，提高了系统的鲁棒性和可扩展性。通过LLM验证步骤，有效减少了LLM的幻觉问题。

**关键设计**：混合相似度量中，具体使用了哪些相似度算法（例如，编辑距离、Jaccard系数、余弦相似度等）以及它们的权重是如何确定的（未知）。LLM验证步骤中，使用了什么样的prompt工程技巧来引导LLM进行准确的判断（未知）。表格转换为键值对文本格式的具体方法（例如，如何处理表格中的合并单元格和复杂布局）（未知）。

## 📊 实验亮点

AutoPK在包含605个PK表格的真实数据集上进行了评估，结果表明其性能显著优于直接使用LLM的基线方法。例如，AutoPK与LLaMA 3.1-70B在半衰期参数上实现了0.92的F1分数，在清除率参数上实现了0.91的F1分数，分别优于直接使用LLaMA 3.1-70B的0.10和0.21。更重要的是，AutoPK使得Gemma 3-27B等开源模型能够超越GPT-4o Mini等商业系统在某些PK参数上的表现，并且显著降低了小模型的幻觉率。

## 🎯 应用场景

AutoPK可广泛应用于兽医药理学、药物安全性监测和公共卫生决策等领域。它能够自动化地从大量的科学文献和报告中提取关键的PK数据，加速药物研发过程，提高监管效率，并为公共卫生政策的制定提供可靠的数据支持。该研究的成果有助于推动药物研发领域的智能化和自动化。

## 📄 摘要（原文）

> Pharmacokinetics (PK) plays a critical role in drug development and regulatory decision-making for human and veterinary medicine, directly affecting public health through drug safety and efficacy assessments. However, PK data are often embedded in complex, heterogeneous tables with variable structures and inconsistent terminologies, posing significant challenges for automated PK data retrieval and standardization. AutoPK, a novel two-stage framework for accurate and scalable extraction of PK data from complex scientific tables. In the first stage, AutoPK identifies and extracts PK parameter variants using large language models (LLMs), a hybrid similarity metric, and LLM-based validation. The second stage filters relevant rows, converts the table into a key-value text format, and uses an LLM to reconstruct a standardized table. Evaluated on a real-world dataset of 605 PK tables, including captions and footnotes, AutoPK shows significant improvements in precision and recall over direct LLM baselines. For instance, AutoPK with LLaMA 3.1-70B achieved an F1-score of 0.92 on half-life and 0.91 on clearance parameters, outperforming direct use of LLaMA 3.1-70B by margins of 0.10 and 0.21, respectively. Smaller models such as Gemma 3-27B and Phi 3-12B with AutoPK achieved 2-7 fold F1 gains over their direct use, with Gemma's hallucination rates reduced from 60-95% down to 8-14%. Notably, AutoPK enabled open-source models like Gemma 3-27B to outperform commercial systems such as GPT-4o Mini on several PK parameters. AutoPK enables scalable and high-confidence PK data extraction, making it well-suited for critical applications in veterinary pharmacology, drug safety monitoring, and public health decision-making, while addressing heterogeneous table structures and terminology and demonstrating generalizability across key PK parameters. Code and data: https://github.com/hosseinsholehrasa/AutoPK

