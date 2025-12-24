---
layout: default
title: "RLHF-V: Towards Trustworthy MLLMs via Behavior Alignment from Fine-grained Correctional Human Feedback"
---

# RLHF-V: Towards Trustworthy MLLMs via Behavior Alignment from Fine-grained Correctional Human Feedback

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.00849" class="toolbar-btn" target="_blank">📄 arXiv: 2312.00849v2</a>
  <a href="https://arxiv.org/pdf/2312.00849.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.00849v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.00849v2', 'RLHF-V: Towards Trustworthy MLLMs via Behavior Alignment from Fine-grained Correctional Human Feedback')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianyu Yu, Yuan Yao, Haoye Zhang, Taiwen He, Yifeng Han, Ganqu Cui, Jinyi Hu, Zhiyuan Liu, Hai-Tao Zheng, Maosong Sun, Tat-Seng Chua

**分类**: cs.CL, cs.CV

**发布日期**: 2023-12-01 (更新: 2024-03-08)

**备注**: Accepted by CVPR 2024

**🔗 代码/项目**: [GITHUB](https://github.com/RLHF-V/RLHF-V)

---

## 💡 一句话要点

**提出RLHF-V以解决多模态大语言模型的幻觉问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `幻觉问题` `人类反馈` `行为对齐` `可信度提升`

## 📋 核心要点

1. 现有的多模态大语言模型普遍存在幻觉问题，生成的文本缺乏与图像的事实基础，导致其在高风险应用中的不可信性。
2. RLHF-V通过细粒度的纠正性人类反馈收集人类偏好，并进行密集的直接偏好优化，从而提升模型的可信度。
3. 在五个基准测试中，RLHF-V显著降低了基线模型的幻觉率34.8%，并在可信度方面达到了开源MLLM的最新水平。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）在多模态理解、推理和交互方面展现了令人印象深刻的能力。然而，现有的MLLMs普遍存在严重的幻觉问题，生成的文本与相关图像缺乏事实基础，导致其在现实世界（尤其是高风险）应用中不可信。为了解决这一挑战，本文提出了RLHF-V，通过细粒度的纠正性人类反馈进行行为对齐，从而增强MLLM的可信度。RLHF-V以段落级别的纠正形式收集人类偏好，并对人类反馈进行密集的直接偏好优化。综合在五个基准上的自动和人工评估实验表明，RLHF-V显著提高了MLLM的可信度，并在数据和计算效率上表现出色。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大语言模型（MLLMs）在生成文本时出现的幻觉问题，现有方法在处理这一问题时效果不佳，导致生成内容不可信。

**核心思路**：RLHF-V的核心思路是通过细粒度的纠正性人类反馈来进行行为对齐，收集人类对幻觉内容的偏好，并进行优化，以提升模型的可信度。

**技术框架**：RLHF-V的整体架构包括数据收集、偏好优化和模型训练三个主要模块。首先收集人类反馈，然后基于这些反馈进行偏好优化，最后更新模型以提高其生成文本的可信度。

**关键创新**：RLHF-V的关键创新在于通过段落级别的纠正性反馈进行密集优化，这种方法与传统的全局优化方法本质上不同，能够更精确地对抗幻觉问题。

**关键设计**：在关键设计上，RLHF-V使用了特定的损失函数来量化人类反馈的偏好，并在模型训练中引入了新的参数设置，以确保优化过程的有效性和效率。具体的网络结构和参数设置在论文中进行了详细描述。

## 📊 实验亮点

实验结果显示，RLHF-V在使用1400个标注样本的情况下，显著降低了基线模型的幻觉率34.8%。此外，RLHF-V在可信度方面超越了使用10000个标注样本的LLaVA-RLHF，且在防止因过度泛化引起的幻觉方面表现出比GPT-4V更好的鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗影像分析、自动驾驶系统和智能客服等高风险场景。在这些领域中，模型的可信度至关重要，RLHF-V的提出有助于提高多模态系统的可靠性和实用性，未来可能推动相关技术的广泛应用。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) have recently demonstrated impressive capabilities in multimodal understanding, reasoning, and interaction. However, existing MLLMs prevalently suffer from serious hallucination problems, generating text that is not factually grounded in associated images. The problem makes existing MLLMs untrustworthy and thus impractical in real-world (especially high-stakes) applications. To address the challenge, we present RLHF-V, which enhances MLLM trustworthiness via behavior alignment from fine-grained correctional human feedback. Specifically, RLHF-V collects human preference in the form of segment-level corrections on hallucinations, and performs dense direct preference optimization over the human feedback. Comprehensive experiments on five benchmarks in both automatic and human evaluation show that, RLHF-V can enable substantially more trustworthy MLLM behaviors with promising data and computation efficiency. Remarkably, using 1.4k annotated data samples, RLHF-V significantly reduces the hallucination rate of the base MLLM by 34.8%, outperforming the concurrent LLaVA-RLHF trained on 10k annotated data. The final model achieves state-of-the-art performance in trustworthiness among open-source MLLMs, and shows better robustness than GPT-4V in preventing hallucinations aroused from over-generalization. We open-source our code, model, and data at https://github.com/RLHF-V/RLHF-V.

