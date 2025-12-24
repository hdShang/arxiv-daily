---
layout: default
title: "Doctor Approved: Generating Medically Accurate Skin Disease Images through AI-Expert Feedback"
---

# Doctor Approved: Generating Medically Accurate Skin Disease Images through AI-Expert Feedback

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12323" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12323v2</a>
  <a href="https://arxiv.org/pdf/2506.12323.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12323v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12323v2', 'Doctor Approved: Generating Medically Accurate Skin Disease Images through AI-Expert Feedback')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Janet Wang, Yunbei Zhang, Zhengming Ding, Jihun Hamm

**分类**: cs.CV

**发布日期**: 2025-06-14 (更新: 2025-10-21)

**备注**: NeurIPS 2025

---

## 💡 一句话要点

**提出MAGIC框架以生成医学准确的皮肤病图像**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学图像生成` `皮肤病诊断` `多模态大语言模型` `数据增强` `专家反馈`

## 📋 核心要点

1. 现有的医学图像生成方法常常生成不准确的图像，导致诊断模型性能下降，尤其在数据稀缺的情况下更为明显。
2. 本文提出MAGIC框架，通过将专家反馈转化为图像合成的可操作标准，显著提高合成图像的临床准确性，同时减少人力负担。
3. 实验结果显示，合成的皮肤病图像与皮肤科医生的评估高度一致，且在20种皮肤病分类任务中，诊断准确率分别提升9.02%和13.89%。

## 📝 摘要（中文）

医学数据的稀缺严重限制了诊断机器学习模型的泛化能力，无法全面代表疾病的变异性。为了解决这一问题，扩散模型被视为合成图像生成和增强的有前景的途径。然而，现有方法常常生成医学不准确的图像，影响模型性能。本文提出了一种新框架MAGIC（通过AI-专家协作生成医学准确图像），利用多模态大语言模型的视觉推理能力，将专家定义的标准转化为可操作的反馈，从而合成临床准确的皮肤病图像。实验表明，使用合成图像增强训练数据可提高诊断准确率，分别提升9.02%和13.89%。

## 🔬 方法详解

**问题定义**：本文旨在解决医学图像生成中的数据稀缺问题，现有方法生成的图像常常缺乏医学准确性，影响了诊断模型的性能。

**核心思路**：MAGIC框架通过利用多模态大语言模型的视觉推理能力，将专家的反馈转化为图像合成的标准，从而生成符合临床要求的皮肤病图像。

**技术框架**：MAGIC框架包括数据收集、专家反馈整合、图像合成和评估四个主要模块。首先收集临床数据，然后将专家反馈转化为合成标准，最后生成图像并进行评估。

**关键创新**：MAGIC框架的创新在于将专家反馈直接融入图像合成过程，避免了传统方法中对复杂奖励函数的依赖，显著提高了合成图像的医学准确性。

**关键设计**：在设计中，采用了多模态大语言模型作为评估工具，结合特定的损失函数来优化合成图像的质量，同时减少了对专家评估的需求。具体参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，MAGIC框架生成的皮肤病图像在临床质量上显著优于传统方法，合成图像与皮肤科医生的评估高度一致。此外，通过将这些合成图像用于训练，诊断准确率在20种皮肤病分类任务中提升了9.02%，在少样本设置下提升了13.89%。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在医学影像学和皮肤病诊断领域。通过生成高质量的合成图像，可以有效增强训练数据集，提高机器学习模型的诊断能力，进而改善临床决策支持系统的性能。未来，该方法还可扩展到其他医学领域的图像生成与分析中。

## 📄 摘要（原文）

> Paucity of medical data severely limits the generalizability of diagnostic ML models, as the full spectrum of disease variability can not be represented by a small clinical dataset. To address this, diffusion models (DMs) have been considered as a promising avenue for synthetic image generation and augmentation. However, they frequently produce medically inaccurate images, deteriorating the model performance. Expert domain knowledge is critical for synthesizing images that correctly encode clinical information, especially when data is scarce and quality outweighs quantity. Existing approaches for incorporating human feedback, such as reinforcement learning (RL) and Direct Preference Optimization (DPO), rely on robust reward functions or demand labor-intensive expert evaluations. Recent progress in Multimodal Large Language Models (MLLMs) reveals their strong visual reasoning capabilities, making them adept candidates as evaluators. In this work, we propose a novel framework, coined MAGIC (Medically Accurate Generation of Images through AI-Expert Collaboration), that synthesizes clinically accurate skin disease images for data augmentation. Our method creatively translates expert-defined criteria into actionable feedback for image synthesis of DMs, significantly improving clinical accuracy while reducing the direct human workload. Experiments demonstrate that our method greatly improves the clinical quality of synthesized skin disease images, with outputs aligning with dermatologist assessments. Additionally, augmenting training data with these synthesized images improves diagnostic accuracy by +9.02% on a challenging 20-condition skin disease classification task, and by +13.89% in the few-shot setting.

