---
layout: default
title: "Toward Better EHR Reasoning in LLMs: Reinforcement Learning with Expert Attention Guidance"
---

# Toward Better EHR Reasoning in LLMs: Reinforcement Learning with Expert Attention Guidance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13579" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13579v1</a>
  <a href="https://arxiv.org/pdf/2508.13579.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13579v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13579v1', 'Toward Better EHR Reasoning in LLMs: Reinforcement Learning with Expert Attention Guidance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yue Fang, Yuxin Guo, Jiaran Gao, Hongxin Ding, Xinke Jiang, Weibin Liao, Yongxin Xu, Yinghao Zhu, Zhibang Yang, Liantao Ma, Junfeng Zhao, Yasha Wang

**分类**: cs.AI

**发布日期**: 2025-08-19

**🔗 代码/项目**: [GITHUB](https://github.com/devilran6/EAG-RL)

---

## 💡 一句话要点

**提出EAG-RL以解决LLMs在EHR推理中的不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `电子健康记录` `大型语言模型` `强化学习` `专家模型` `临床预测` `推理能力` `数据分析`

## 📋 核心要点

1. 现有方法在EHR推理任务中表现不佳，主要由于高维数据的时间结构建模困难。
2. 本文提出EAG-RL框架，通过专家模型指导的强化学习来提升LLMs的推理能力。
3. 在真实EHR数据集上，EAG-RL使LLMs的推理能力平均提升14.62%，并增强了对特征扰动的鲁棒性。

## 📝 摘要（中文）

提高大型语言模型（LLMs）在电子健康记录（EHR）推理中的能力对于实现准确且可推广的临床预测至关重要。尽管LLMs在医学文本理解方面表现出色，但在基于EHR的预测任务中表现不佳，主要由于高维数据的时间结构建模挑战。现有方法通常依赖于混合范式，LLMs仅作为固定的检索器，而下游深度学习模型负责预测，未能提升LLMs的内在推理能力。为此，本文提出了一种新颖的两阶段训练框架EAG-RL，通过专家注意力指导来增强LLMs的EHR推理能力。实验结果表明，EAG-RL在两个真实EHR数据集上的表现提升了14.62%。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在电子健康记录推理中的不足，现有方法未能有效提升LLMs的内在推理能力，且在处理高维时间结构数据时存在局限性。

**核心思路**：EAG-RL框架通过专家模型的注意力指导，利用强化学习优化LLMs的推理策略，从而提升其在EHR推理任务中的表现。

**技术框架**：EAG-RL包括两个主要阶段：第一阶段使用专家指导的蒙特卡罗树搜索构建高质量的逐步推理轨迹，以初始化LLMs的策略；第二阶段通过强化学习进一步优化策略，使LLMs的注意力与专家模型识别的临床特征对齐。

**关键创新**：EAG-RL的核心创新在于结合专家模型的注意力指导与强化学习，显著提升了LLMs在EHR推理中的内在能力，与传统方法相比，避免了对下游深度学习模型的依赖。

**关键设计**：在EAG-RL中，关键参数包括专家模型的选择和训练过程，损失函数设计用于优化LLMs的注意力分布，以确保其关注临床相关特征。

## 📊 实验亮点

EAG-RL在两个真实EHR数据集上的实验结果显示，LLMs的EHR推理能力平均提升了14.62%。此外，该方法增强了模型对特征扰动的鲁棒性，并提高了在未见临床领域的泛化能力，展示了其在实际应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括临床决策支持系统和个性化医疗，能够帮助医生更准确地进行临床预测和诊断。未来，EAG-RL有望在更广泛的医疗数据分析和智能健康管理中发挥重要作用，推动医疗AI的发展。

## 📄 摘要（原文）

> Improving large language models (LLMs) for electronic health record (EHR) reasoning is essential for enabling accurate and generalizable clinical predictions. While LLMs excel at medical text understanding, they underperform on EHR-based prediction tasks due to challenges in modeling temporally structured, high-dimensional data. Existing approaches often rely on hybrid paradigms, where LLMs serve merely as frozen prior retrievers while downstream deep learning (DL) models handle prediction, failing to improve the LLM's intrinsic reasoning capacity and inheriting the generalization limitations of DL models. To this end, we propose EAG-RL, a novel two-stage training framework designed to intrinsically enhance LLMs' EHR reasoning ability through expert attention guidance, where expert EHR models refer to task-specific DL models trained on EHR data. Concretely, EAG-RL first constructs high-quality, stepwise reasoning trajectories using expert-guided Monte Carlo Tree Search to effectively initialize the LLM's policy. Then, EAG-RL further optimizes the policy via reinforcement learning by aligning the LLM's attention with clinically salient features identified by expert EHR models. Extensive experiments on two real-world EHR datasets show that EAG-RL improves the intrinsic EHR reasoning ability of LLMs by an average of 14.62%, while also enhancing robustness to feature perturbations and generalization to unseen clinical domains. These results demonstrate the practical potential of EAG-RL for real-world deployment in clinical prediction tasks. Our code have been available at https://github.com/devilran6/EAG-RL.

