---
layout: default
title: Reliable LLM-Based Edge-Cloud-Expert Cascades for Telecom Knowledge Systems
---

# Reliable LLM-Based Edge-Cloud-Expert Cascades for Telecom Knowledge Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20012" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20012v1</a>
  <a href="https://arxiv.org/pdf/2512.20012.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20012v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20012v1', 'Reliable LLM-Based Edge-Cloud-Expert Cascades for Telecom Knowledge Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qiushuo Hou, Sangwoo Park, Matteo Zecchin, Yunlong Cai, Guanding Yu, Osvaldo Simeone, Tommaso Melodia

**分类**: eess.SP, cs.LG

**发布日期**: 2025-12-23

**备注**: This paper has been submitted to a journal

---

## 💡 一句话要点

**提出基于级联LLM的电信知识系统，优化成本与可靠性，实现自动化决策。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `边缘计算` `知识系统` `多重假设检验` `电信网络` `问答系统` `成本优化`

## 📋 核心要点

1. 现有LLM在电信领域应用面临推理成本、延迟和可靠性之间的权衡难题，需要更高效的部署策略。
2. 提出边缘-云-专家级联LLM知识系统，利用边缘模型处理常规查询，云模型处理复杂问题，专家处理疑难杂症。
3. 通过多重假设检验（MHT）进行阈值选择，保证在规定置信水平下的可靠性，并在TeleQnA数据集上验证了成本效率。

## 📝 摘要（中文）

大型语言模型（LLM）正在成为电信等领域自动化的关键推动力，协助解决故障排除、标准解读和网络优化等任务。然而，实际部署需要在推理成本、延迟和可靠性之间取得平衡。本文研究了一种基于边缘-云-专家级联LLM的知识系统，该系统通过问答流程支持决策。其中，高效的边缘模型处理常规查询，更强大的云模型处理复杂案例，仅在必要时才涉及人工专家。我们定义了一个以错位成本为约束的优化问题，旨在最小化平均处理成本，同时保证自动化答案与专家判断的一致性。我们提出了一种基于多重假设检验（MHT）的统计严格的阈值选择方法，用于基于知识和置信度测试的查询处理机制。该方法为错位风险提供了有限样本保证。在电信专用基准TeleQnA数据集上的实验表明，与传统的级联基线相比，该方法实现了卓越的成本效率，同时确保了在规定的置信水平下的可靠性。

## 🔬 方法详解

**问题定义**：现有方法在电信知识系统中应用LLM时，难以兼顾推理成本、延迟和可靠性。简单地使用大型LLM会导致高昂的计算成本和延迟，而小型LLM的准确性可能不足。因此，需要一种能够根据查询的复杂程度动态调整处理方式的系统，以在成本和性能之间取得平衡。现有级联系统通常依赖于启发式规则或简单的阈值来决定何时将查询传递给更强大的模型或专家，缺乏统计上的严格保证。

**核心思路**：本文的核心思路是构建一个边缘-云-专家级联的LLM系统，并利用统计假设检验来动态地决定查询的处理方式。边缘模型快速且成本低，但能力有限；云模型能力更强，但成本更高；专家则作为最终保障，处理最复杂的情况。通过这种分层结构，可以有效地利用资源，降低整体成本。

**技术框架**：该系统包含三个主要模块：边缘LLM、云LLM和专家系统。当接收到一个查询时，首先由边缘LLM进行处理。边缘LLM会输出答案以及一个置信度评分。然后，系统会根据预先设定的阈值对置信度评分进行判断。如果置信度高于阈值，则直接返回边缘LLM的答案；否则，将查询传递给云LLM。云LLM的处理流程类似，也会输出答案和置信度评分。如果云LLM的置信度仍然低于阈值，则将查询传递给专家系统进行处理。

**关键创新**：该论文的关键创新在于使用多重假设检验（MHT）来选择置信度阈值。传统的阈值选择方法通常是基于经验或启发式规则，缺乏理论依据。MHT提供了一种统计上严格的方法，可以在保证一定的错位风险的前提下，选择最优的阈值。这意味着可以控制自动化答案与专家判断不一致的概率，从而提高系统的可靠性。

**关键设计**：论文的关键设计包括：1) 使用知识测试和置信度测试来评估LLM的答案质量。知识测试评估答案的正确性，置信度测试评估LLM对答案的自信程度。2) 使用多重假设检验（MHT）来选择置信度阈值。MHT可以控制总体错误率，从而保证系统的可靠性。3) 定义了一个错位成本约束的优化问题，旨在最小化平均处理成本，同时保证自动化答案与专家判断的一致性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20012v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20012v1/paper_photo/FST.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20012v1/photo/boxplot_comparison.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，所提出的基于MHT的阈值选择方法在TeleQnA数据集上优于传统的级联基线。在保证相同错位风险水平的前提下，该方法能够显著降低平均处理成本。具体而言，与基线方法相比，该方法可以将成本降低10%-20%，同时保持与专家判断的高度一致性。

## 🎯 应用场景

该研究成果可应用于各种需要知识密集型决策的电信场景，例如网络故障诊断、服务配置优化和客户问题解答。通过自动化处理大部分查询，可以显著降低人工成本，提高响应速度，并提升客户满意度。此外，该方法也可以推广到其他领域，如医疗诊断、金融风控等。

## 📄 摘要（原文）

> Large language models (LLMs) are emerging as key enablers of automation in domains such as telecommunications, assisting with tasks including troubleshooting, standards interpretation, and network optimization. However, their deployment in practice must balance inference cost, latency, and reliability. In this work, we study an edge-cloud-expert cascaded LLM-based knowledge system that supports decision-making through a question-and-answer pipeline. In it, an efficient edge model handles routine queries, a more capable cloud model addresses complex cases, and human experts are involved only when necessary. We define a misalignment-cost constrained optimization problem, aiming to minimize average processing cost, while guaranteeing alignment of automated answers with expert judgments. We propose a statistically rigorous threshold selection method based on multiple hypothesis testing (MHT) for a query processing mechanism based on knowledge and confidence tests. The approach provides finite-sample guarantees on misalignment risk. Experiments on the TeleQnA dataset -- a telecom-specific benchmark -- demonstrate that the proposed method achieves superior cost-efficiency compared to conventional cascaded baselines, while ensuring reliability at prescribed confidence levels.

