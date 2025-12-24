---
layout: default
title: Vid-SME: Membership Inference Attacks against Large Video Understanding Models
---

# Vid-SME: Membership Inference Attacks against Large Video Understanding Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.03179" class="toolbar-btn" target="_blank">📄 arXiv: 2506.03179v1</a>
  <a href="https://arxiv.org/pdf/2506.03179.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.03179v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.03179v1', 'Vid-SME: Membership Inference Attacks against Large Video Understanding Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qi Li, Runpeng Yu, Xinchao Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-29

---

## 💡 一句话要点

**提出Vid-SME以解决视频理解模型的成员推断攻击问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频理解` `成员推断攻击` `Sharma-Mittal熵` `多模态模型` `数据隐私` `深度学习`

## 📋 核心要点

1. 现有的成员推断攻击方法在视频领域的扩展性差，无法有效捕捉视频帧的时间变化，导致低真阳性率。
2. 本文提出Vid-SME，利用模型输出的置信度和自适应参数化计算Sharma-Mittal熵，以生成视频的成员评分。
3. 在多种自训练和开源视频理解模型上进行的实验表明，Vid-SME显著提升了成员推断的有效性。

## 📝 摘要（中文）

多模态大型语言模型（MLLMs）在处理复杂的多模态任务方面表现出色，广泛应用于视频理解。然而，这些模型的快速发展引发了严重的数据隐私问题，尤其是训练数据集中可能包含敏感视频内容。现有的成员推断攻击（MIAs）方法在视频领域的适用性不足，主要由于未能有效捕捉视频帧的时间变化。为了解决这一挑战，本文提出了Vid-SME，这是首个针对视频数据的成员推断方法，利用模型输出的置信度和自适应参数化计算Sharma-Mittal熵（SME），通过自然视频帧与时间反转视频帧之间的SME差异，生成稳健的成员评分。实验结果表明，Vid-SME在多种自训练和开源视频理解模型上表现出强大的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有成员推断攻击方法在视频理解模型中的不足，尤其是其在处理视频帧时间变化时的低效性和扩展性问题。

**核心思路**：Vid-SME通过结合模型输出的置信度和自适应参数化，计算视频输入的Sharma-Mittal熵，利用自然视频帧与时间反转帧之间的熵差异来生成成员评分。

**技术框架**：Vid-SME的整体架构包括数据预处理、模型输出置信度计算、Sharma-Mittal熵计算和成员评分生成四个主要模块。

**关键创新**：Vid-SME是首个专为视频数据设计的成员推断方法，能够有效捕捉视频帧的时间变化，显著提高了成员推断的准确性。

**关键设计**：在设计中，Vid-SME采用自适应参数化策略，优化了熵计算过程，并通过实验验证了不同帧数对模型行为的影响。通过这些设计，Vid-SME在低假阳性率下实现了更高的真阳性率。

## 📊 实验亮点

实验结果显示，Vid-SME在多个自训练和开源视频理解模型上显著提高了成员推断的准确性，尤其是在低假阳性率下实现了更高的真阳性率，展现出强大的有效性和实用性。

## 🎯 应用场景

Vid-SME的研究成果在视频理解领域具有广泛的应用潜力，尤其是在涉及敏感视频内容的场景中，如个人隐私保护和监控视频分析。通过提高对训练数据的成员推断能力，Vid-SME能够帮助开发更安全的多模态模型，减少数据泄露风险，推动隐私保护技术的发展。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) demonstrate remarkable capabilities in handling complex multimodal tasks and are increasingly adopted in video understanding applications. However, their rapid advancement raises serious data privacy concerns, particularly given the potential inclusion of sensitive video content, such as personal recordings and surveillance footage, in their training datasets. Determining improperly used videos during training remains a critical and unresolved challenge. Despite considerable progress on membership inference attacks (MIAs) for text and image data in MLLMs, existing methods fail to generalize effectively to the video domain. These methods suffer from poor scalability as more frames are sampled and generally achieve negligible true positive rates at low false positive rates (TPR@Low FPR), mainly due to their failure to capture the inherent temporal variations of video frames and to account for model behavior differences as the number of frames varies. To address these challenges, we introduce Vid-SME, the first membership inference method tailored for video data used in video understanding LLMs (VULLMs). Vid-SME leverages the confidence of model output and integrates adaptive parameterization to compute Sharma-Mittal entropy (SME) for video inputs. By leveraging the SME difference between natural and temporally-reversed video frames, Vid-SME derives robust membership scores to determine whether a given video is part of the model's training set. Experiments on various self-trained and open-sourced VULLMs demonstrate the strong effectiveness of Vid-SME.

