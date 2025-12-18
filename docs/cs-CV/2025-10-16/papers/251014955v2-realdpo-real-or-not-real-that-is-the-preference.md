---
layout: default
title: RealDPO: Real or Not Real, that is the Preference
---

# RealDPO: Real or Not Real, that is the Preference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.14955" class="toolbar-btn" target="_blank">📄 arXiv: 2510.14955v2</a>
  <a href="https://arxiv.org/pdf/2510.14955.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14955v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.14955v2', 'RealDPO: Real or Not Real, that is the Preference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guo Cheng, Danni Yang, Ziqi Huang, Jianlou Si, Chenyang Si, Ziwei Liu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-16 (更新: 2025-11-06)

**备注**: Code:https://github.com/Vchitect/RealDPO Project Page:https://vchitect.github.io/RealDPO-Project/

---

## 💡 一句话要点

**RealDPO：利用真实数据偏好学习，提升视频生成模型运动真实性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `视频生成` `运动合成` `偏好学习` `直接偏好优化` `DPO` `真实数据` `RealAction-5K`

## 📋 核心要点

1. 现有视频生成模型在复杂运动生成方面存在不足，难以产生自然流畅且符合上下文的运动。
2. RealDPO利用真实世界数据作为正样本，通过直接偏好优化（DPO）进行迭代自校正，提升运动真实性。
3. RealDPO在视频质量、文本对齐和运动真实感方面，均优于现有模型和偏好优化技术，并提出了RealAction-5K数据集。

## 📝 摘要（中文）

视频生成模型在合成质量方面取得了显著进展。然而，生成复杂的运动仍然是一个关键挑战，因为现有模型通常难以产生自然、流畅和上下文一致的运动。生成运动与真实世界运动之间的差距限制了它们的实际应用。为了解决这个问题，我们引入了RealDPO，一种新颖的对齐范式，它利用真实世界的数据作为偏好学习的积极样本，从而实现更准确的运动合成。与提供有限纠正反馈的传统监督微调（SFT）不同，RealDPO采用直接偏好优化（DPO）与定制的损失函数来增强运动的真实感。通过将真实世界的视频与错误的模型输出进行对比，RealDPO实现了迭代自校正，逐步提高运动质量。为了支持复杂运动合成中的后训练，我们提出了RealAction-5K，这是一个精心策划的高质量视频数据集，捕捉了人类日常活动，具有丰富而精确的运动细节。大量的实验表明，与最先进的模型和现有的偏好优化技术相比，RealDPO显著提高了视频质量、文本对齐和运动真实感。

## 🔬 方法详解

**问题定义**：论文旨在解决视频生成模型在生成复杂运动时，运动不自然、不流畅以及缺乏上下文一致性的问题。现有方法，如监督微调（SFT），提供的纠正反馈有限，难以有效提升运动的真实感。

**核心思路**：论文的核心思路是利用真实世界的数据作为正样本，通过偏好学习的方式，让模型学习区分真实运动和模型生成的错误运动，从而提升生成运动的真实性。这种方法避免了直接模仿真实数据，而是通过对比学习的方式，让模型学习运动的内在规律。

**技术框架**：RealDPO的技术框架主要包括以下几个部分：首先，使用预训练的视频生成模型生成初始的视频。然后，将生成的视频与真实视频进行对比，利用DPO算法进行优化。DPO算法使用一个定制的损失函数，该损失函数鼓励模型生成更接近真实运动的视频。最后，通过迭代的方式，不断优化模型，提升生成视频的运动真实性。同时，论文还提出了RealAction-5K数据集，用于支持复杂运动合成的后训练。

**关键创新**：RealDPO的关键创新在于将直接偏好优化（DPO）应用于视频生成模型的运动真实性提升。与传统的监督学习方法不同，DPO不需要显式的标签，而是通过对比真实数据和生成数据，让模型学习偏好。此外，RealDPO还提出了一个定制的损失函数，该损失函数能够更好地衡量生成运动的真实性。

**关键设计**：RealDPO的关键设计包括：1) 使用DPO算法进行优化，避免了显式标签的需求；2) 设计了一个定制的损失函数，用于衡量生成运动的真实性；3) 提出了RealAction-5K数据集，用于支持复杂运动合成的后训练。具体的参数设置和网络结构等技术细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，RealDPO在视频质量、文本对齐和运动真实感方面均优于现有方法。与最先进的模型和现有的偏好优化技术相比，RealDPO取得了显著的提升。例如，在运动真实感方面，RealDPO的指标提升了XX%，证明了其有效性。RealAction-5K数据集的发布也为后续研究提供了有力支持。

## 🎯 应用场景

RealDPO技术可应用于各种视频生成领域，例如游戏开发、电影制作、虚拟现实和增强现实等。它可以帮助生成更逼真、更自然的虚拟人物和场景，提升用户体验。该技术还有潜力应用于机器人控制领域，使机器人能够更自然地执行复杂的运动任务。未来，该技术有望推动视频生成和机器人控制等领域的发展。

## 📄 摘要（原文）

> Video generative models have recently achieved notable advancements in synthesis quality. However, generating complex motions remains a critical challenge, as existing models often struggle to produce natural, smooth, and contextually consistent movements. This gap between generated and real-world motions limits their practical applicability. To address this issue, we introduce RealDPO, a novel alignment paradigm that leverages real-world data as positive samples for preference learning, enabling more accurate motion synthesis. Unlike traditional supervised fine-tuning (SFT), which offers limited corrective feedback, RealDPO employs Direct Preference Optimization (DPO) with a tailored loss function to enhance motion realism. By contrasting real-world videos with erroneous model outputs, RealDPO enables iterative self-correction, progressively refining motion quality. To support post-training in complex motion synthesis, we propose RealAction-5K, a curated dataset of high-quality videos capturing human daily activities with rich and precise motion details. Extensive experiments demonstrate that RealDPO significantly improves video quality, text alignment, and motion realism compared to state-of-the-art models and existing preference optimization techniques.

