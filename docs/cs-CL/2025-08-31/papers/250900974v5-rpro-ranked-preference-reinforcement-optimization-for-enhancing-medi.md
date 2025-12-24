---
layout: default
title: "RPRO: Ranked Preference Reinforcement Optimization for Enhancing Medical QA and Diagnostic Reasoning"
---

# RPRO: Ranked Preference Reinforcement Optimization for Enhancing Medical QA and Diagnostic Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00974" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00974v5</a>
  <a href="https://arxiv.org/pdf/2509.00974.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00974v5" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00974v5', 'RPRO: Ranked Preference Reinforcement Optimization for Enhancing Medical QA and Diagnostic Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chia-Hsuan Hsu, Jun-En Ding, Hsin-Ling Hsu, Chih-Ho Hsu, Li-Hung Yao, Chun-Chieh Liao, Feng Liu, Fang-Ming Hung

**分类**: cs.CL

**发布日期**: 2025-08-31 (更新: 2025-12-07)

---

## 💡 一句话要点

**提出RPRO以解决医疗问答中的推理准确性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医疗问答` `推理优化` `强化学习` `临床决策` `大型语言模型` `偏好驱动` `组排名优化`

## 📋 核心要点

1. 现有的大型语言模型在医疗问答中生成的推理链缺乏事实准确性和临床可靠性，影响了其应用效果。
2. 本文提出了RPRO框架，通过结合强化学习与偏好驱动的推理优化，提升了临床推理链的性能。
3. 实验结果显示，RPRO在多个数据集上均优于强基线模型，尤其是我们的2B参数模型超越了更大规模的模型。

## 📝 摘要（中文）

医疗问答需要将领域知识与逻辑推理相结合的高级推理能力。然而，现有的大型语言模型（LLMs）常常生成缺乏事实准确性和临床可靠性的推理链。本文提出了排名偏好强化优化（RPRO），一个结合强化学习与偏好驱动推理优化的新框架，以提升临床推理链的表现。RPRO通过采用任务自适应推理模板和概率评估机制，使模型输出与既定临床工作流程对齐，同时自动识别和纠正低质量推理链。与传统的成对偏好方法不同，RPRO引入了基于Bradley-Terry模型的组排名优化，并结合KL散度正则化以实现稳定训练。实验结果表明，在PubMedQA、MedQA-USMLE和来自远东纪念医院的真实临床数据集上，RPRO在强基线模型上实现了一致的提升。值得注意的是，我们的2B参数模型超越了更大规模的7B-20B模型，包括医学专业化变体。这些发现表明，将偏好优化与质量驱动的优化相结合，为构建更可靠的医疗LLMs提供了一种可扩展且临床基础的方法。

## 🔬 方法详解

**问题定义**：本文旨在解决医疗问答中推理链的准确性和可靠性问题。现有方法常常生成低质量的推理链，导致临床应用效果不佳。

**核心思路**：RPRO框架通过结合强化学习与偏好驱动的推理优化，利用任务自适应推理模板和概率评估机制，提升推理链的质量与准确性。

**技术框架**：RPRO的整体架构包括三个主要模块：任务自适应推理模板、概率评估机制和组排名优化。首先，模型生成推理链，然后通过评估机制对其进行评分，最后通过组排名优化进行调整和改进。

**关键创新**：RPRO的主要创新在于引入了基于Bradley-Terry模型的组排名优化方法，区别于传统的成对偏好方法，同时结合KL散度正则化以实现训练的稳定性。

**关键设计**：在模型设计中，采用了任务自适应的推理模板，损失函数中引入了KL散度正则化，并通过组排名优化来提升推理链的整体质量。

## 📊 实验亮点

实验结果表明，RPRO在PubMedQA和MedQA-USMLE等数据集上均显著优于强基线模型，尤其是我们的2B参数模型在性能上超越了7B-20B的更大模型，显示出RPRO在医疗问答中的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括医疗问答系统、临床决策支持工具和医学教育等。通过提升医疗LLMs的推理准确性和可靠性，RPRO能够为医生和患者提供更为精准的信息支持，进而改善医疗服务质量。未来，该方法有望在更广泛的医疗场景中推广应用，推动智能医疗的发展。

## 📄 摘要（原文）

> Medical question answering requires advanced reasoning that integrates domain knowledge with logical inference. However, existing large language models (LLMs) often generate reasoning chains that lack factual accuracy and clinical reliability. We propose Ranked Preference Reinforcement Optimization (RPRO), a novel framework that combines reinforcement learning with preference-driven reasoning refinement to enhance clinical chain-of-thought (CoT) performance. RPRO distinguishes itself from prior approaches by employing task-adaptive reasoning templates and a probabilistic evaluation mechanism that aligns model outputs with established clinical workflows, while automatically identifying and correcting low-quality reasoning chains. Unlike traditional pairwise preference methods, RPRO introduces a groupwise ranking optimization based on the Bradley--Terry model and incorporates KL-divergence regularization for stable training. Experiments on PubMedQA, MedQA-USMLE, and a real-world clinical dataset from Far Eastern Memorial Hospital (FEMH) demonstrate consistent improvements over strong baselines. Remarkably, our 2B-parameter model outperforms much larger 7B--20B models, including medical-specialized variants. These findings demonstrate that combining preference optimization with quality-driven refinement provides a scalable and clinically grounded approach to building more reliable medical LLMs.

