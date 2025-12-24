---
layout: default
title: KG-TRACES: Enhancing Large Language Models with Knowledge Graph-constrained Trajectory Reasoning and Attribution Supervision
---

# KG-TRACES: Enhancing Large Language Models with Knowledge Graph-constrained Trajectory Reasoning and Attribution Supervision

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00783" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00783v2</a>
  <a href="https://arxiv.org/pdf/2506.00783.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00783v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00783v2', 'KG-TRACES: Enhancing Large Language Models with Knowledge Graph-constrained Trajectory Reasoning and Attribution Supervision')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rong Wu, Pinlong Cai, Jianbiao Mei, Licheng Wen, Tao Hu, Xuemeng Yang, Daocheng Fu, Botian Shi

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-01 (更新: 2025-10-20)

**备注**: 24 pages, 13 figures

**🔗 代码/项目**: [GITHUB](https://github.com/Edaizi/KG-TRACES)

---

## 💡 一句话要点

**提出KG-TRACES以解决大语言模型推理可解释性不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识图谱` `推理能力` `可解释性` `归因监督` `自然语言处理` `复杂推理` `模型优化`

## 📋 核心要点

1. 现有大型语言模型在复杂推理任务中缺乏可解释性，导致推理过程不透明，影响其应用。
2. KG-TRACES框架通过显式监督推理路径，提升模型的推理能力，支持知识图谱可用和不可用的场景。
3. 实验结果显示，KG-TRACES在WebQSP和CWQ任务上分别提升了1.6%和4.8%的Hits@1，证明了其有效性。

## 📝 摘要（中文）

大型语言模型（LLMs）在自然语言处理任务中取得了显著进展，但在复杂推理问题上的表现仍受到可解释性和可信度不足的限制。这种问题通常表现为幻觉或无法归因的推理过程，限制了其在复杂推理场景中的应用。为了解决这一问题，本文提出了知识图谱约束的轨迹推理归因与链式解释监督（KG-TRACES）框架，通过对推理路径和过程的显式监督来增强LLMs的推理能力。KG-TRACES共同监督模型预测符号关系路径、完整三元组推理路径，并生成基于推理路径的归因感知推理过程。实验表明，KG-TRACES在复杂推理任务上显著超越现有的最先进方法，展示了其在医学等专业领域的迁移能力。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在复杂推理任务中的可解释性不足问题，现有方法常常导致推理过程的幻觉和不透明性，限制了其在实际应用中的可信度。

**核心思路**：KG-TRACES通过对推理路径的显式监督，增强了模型的推理能力，使其能够在知识图谱可用和不可用的情况下进行合理推理。该设计确保了推理过程的可解释性和可归因性。

**技术框架**：KG-TRACES框架包括三个主要模块：符号关系路径预测、完整三元组推理路径预测和基于推理路径的归因感知推理过程生成。在推理阶段，模型根据知识图谱的可用性选择合适的推理路径。

**关键创新**：KG-TRACES的创新在于引入了对推理路径的显式监督，这与传统方法的隐式学习方式形成了鲜明对比，从而提高了推理的稳定性和目标导向性。

**关键设计**：在模型设计中，采用了特定的损失函数来优化推理路径的预测精度，并通过可视化中间推理步骤来验证推理过程的合理性和准确性。

## 📊 实验亮点

KG-TRACES在复杂推理任务上表现出色，WebQSP任务的Hits@1提升了1.6%，F1提升了4.7%；在CWQ任务上，Hits@1提升了4.8%，F1提升了2.1%。这些结果表明KG-TRACES在推理能力和稳定性方面的显著改进，超越了现有的最先进方法。

## 🎯 应用场景

KG-TRACES的研究成果在多个领域具有广泛的应用潜力，尤其是在需要高可解释性和可信度的复杂推理场景中，如医疗诊断、法律分析和金融决策等。通过提升模型的推理能力和可解释性，该框架有望推动智能系统在实际应用中的普及和信任。

## 📄 摘要（原文）

> Large language models (LLMs) have made remarkable strides in various natural language processing tasks, but their performance on complex reasoning problems remains hindered by a lack of explainability and trustworthiness. This issue, often manifesting as hallucinations or unattributable reasoning processes, limits their applicability in complex reasoning scenarios. To address this, we propose Knowledge Graph-constrained Trajectory Reasoning Attribution and Chain Explanation Supervision (KG-TRACES), a novel framework that enhances the reasoning ability of LLMs through explicit supervision over reasoning paths and processes. KG-TRACES jointly supervises the model to: (1) predict symbolic relation paths, (2) predict full triple-level reasoning paths, and (3) generate attribution-aware reasoning processes grounded in the reasoning paths. At inference phase, the model adapts to both KG-available and KG-unavailable scenarios, retrieving reasoning paths from a KG when possible or predicting plausible reasoning paths with only intrinsic knowledge when not. This design enables the model to reason in an explainable and source-attributable pattern. Through extensive experiments on complex reasoning tasks, we demonstrate that KG-TRACES significantly outperforms existing SOTA: it improves Hits@1 by 1.6% and F1 by 4.7% on WebQSP, and achieves improvements of 4.8% in Hits@1 and 2.1% in F1 on CWQ. Moreover, we show its transferability to specialized domains such as medicine. By visualizing the intermediate steps of reasoning processes, we further show that the explicit supervision introduced by KG-TRACES leads to more stable and goal-directed reasoning processes, aligning closely with correct answers. Code is available at https://github.com/Edaizi/KG-TRACES.

