---
layout: default
title: "POVQA: Preference-Optimized Video Question Answering with Rationales for Data Efficiency"
---

# POVQA: Preference-Optimized Video Question Answering with Rationales for Data Efficiency

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.01009" class="toolbar-btn" target="_blank">📄 arXiv: 2510.01009v1</a>
  <a href="https://arxiv.org/pdf/2510.01009.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01009v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.01009v1', 'POVQA: Preference-Optimized Video Question Answering with Rationales for Data Efficiency')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ashim Dahal, Ankit Ghimire, Saydul Akbar Murad, Nick Rahimi

**分类**: cs.CV, cs.MM

**发布日期**: 2025-10-01

---

## 💡 一句话要点

**提出POVQA：一种数据高效的偏好优化视频问答方法，利用理由提升性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视频问答` `长视频理解` `视觉语言模型` `时序池化` `理由生成` `偏好优化` `数据高效`

## 📋 核心要点

1. 现有基于LVLM的视频问答方法在处理长视频时，受限于上下文窗口大小，无法有效利用视频信息。
2. POVQA通过时序池化将视频帧压缩为低帧率图像，并结合理由生成，提升LVLM在数据有限情况下的性能。
3. 在ReasonVQA数据集上，POVQA显著提升了VQA性能和理由质量，并在不同池化策略下表现出鲁棒性。

## 📝 摘要（中文）

本文提出了一种数据高效的视频问答（VQA）流程POVQA，旨在利用大型视觉语言模型（LVLMs）解决长视频问答问题。该方法将每秒视频压缩成单个时序池化图像（通过运动模糊和加权平均的变体），然后通过轻量级监督对齐LVLMs。具体而言，使用Blend Blur with Last Frame、Weighted Average、Exponential和Ramp池化构建1 fps的输入源，并使用监督两轮目标（包括推理和最终答案）对QWEN-2.5-VL 7B进行微调。在ReasonVQA数据集上，应用监督微调（SFT）和直接偏好优化（DPO），该数据集包含12部电影的239个人工标注的问题-答案对以及推理提示。实验结果表明，该方法显著提高了性能：F1分数从0.212提高到0.543，BLEU-4从0.031提高到0.291，ROUGE-L从0.196提高到0.528。理由质量也显著提高。在各种池化函数上进行的SFT + DPO交叉评估表明，无论训练或测试时使用的池化方案如何，增益都持续存在，表明在时序证据总结方面具有很强的鲁棒性。在TVQA的零样本评估中也观察到了类似的结论。

## 🔬 方法详解

**问题定义**：论文旨在解决长视频问答任务中，现有方法因上下文窗口限制导致的数据利用率低下的问题。现有方法无法有效处理超过50秒的视频，且忽略了视频帧之间的时间相关性，导致信息损失。

**核心思路**：论文的核心思路是通过时序池化将视频压缩成低帧率图像，减少输入序列长度，从而在有限的上下文窗口内处理更长的视频。同时，引入理由生成作为辅助任务，提升模型对视频内容的理解和推理能力。

**技术框架**：POVQA的整体框架包括以下几个阶段：1) 视频预处理：使用不同的时序池化方法（Blend Blur with Last Frame、Weighted Average、Exponential和Ramp pooling）将视频转换为1 fps的图像序列。2) 模型微调：使用QWEN-2.5-VL 7B作为LVLM，采用监督微调（SFT）和直接偏好优化（DPO）进行训练。3) 理由生成：在训练过程中，模型需要生成回答问题的理由，以提高答案的准确性和可解释性。

**关键创新**：论文的关键创新在于：1) 提出了一种数据高效的视频问答流程，通过时序池化减少了计算量。2) 引入理由生成作为辅助任务，提升了模型的推理能力。3) 结合SFT和DPO，优化了模型的偏好，使其更符合人类的认知。

**关键设计**：在时序池化方面，论文尝试了多种方法，包括Blend Blur with Last Frame、Weighted Average、Exponential和Ramp pooling，以探索最佳的压缩策略。在模型训练方面，论文使用了监督微调（SFT）和直接偏好优化（DPO），并设计了包含推理和最终答案的两轮目标。ReasonVQA数据集包含人工标注的问题-答案对以及推理提示，用于训练和评估模型。

## 📊 实验亮点

实验结果表明，POVQA在ReasonVQA数据集上取得了显著的性能提升。F1分数从0.212提高到0.543，BLEU-4从0.031提高到0.291，ROUGE-L从0.196提高到0.528。此外，该方法在不同池化策略下表现出鲁棒性，并在TVQA数据集上实现了零样本迁移。

## 🎯 应用场景

POVQA具有广泛的应用前景，包括智能监控、视频内容分析、教育视频问答、电影理解等领域。该方法可以帮助用户快速理解视频内容，并从中提取关键信息。通过结合理由生成，可以提高问答结果的可信度和可解释性，为用户提供更可靠的决策支持。

## 📄 摘要（原文）

> Video Question Answering (VQA) with Large Vision Language Models (LVLMs) has gained significant traction in research ever since the Flamingo was introduced by Deepmind. Recent advancements in large context/long video question answering have allowed VQA tasks to have context window of 1500+ frames. However, this only leads to 50 seconds of video footage without losing any significant information. We introduce POVQA, a data-efficient pipeline that compresses each second of video into a single temporally pooled image (via motion blur and weighted averaging variants) and then align LVLMs with lightweight supervision. Concretely, we build 1 fps input sources using Blend Blur with Last Frame, Weighted Average, Exponential and Ramp pooling and fine-tune QWEN-2.5-VL 7B with supervised two turn target including reasoning and final answer. We apply Supervised Fine Tuning (SFT) and Direct Preference Optimization (DPO) on our novel dataset ReasonVQA consisting of 12 movies with 239 human annotated question-answer with reasoning prompts. On our ReasonVQA dataset, this method dramatically improves performance over pooled baselines: F1 score improves from 0.212 to 0.543, BLEU-4 from 0.031 to 0.291, and ROUGE-L from 0.196 to 0.528. Rationale quality also significantly increases. Cross-evaluation of SFT + DPO on various pooling functions show that the gains persist regardless of the pooling scheme used at train or test time, indicating strong robustness on summarization of temporal evidence. Similar observations were made on zero-shot in TVQA.

