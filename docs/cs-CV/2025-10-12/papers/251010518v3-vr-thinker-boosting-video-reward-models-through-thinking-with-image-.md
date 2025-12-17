---
layout: default
title: VR-Thinker: Boosting Video Reward Models through Thinking-with-Image Reasoning
---

# VR-Thinker: Boosting Video Reward Models through Thinking-with-Image Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.10518" class="toolbar-btn" target="_blank">📄 arXiv: 2510.10518v3</a>
  <a href="https://arxiv.org/pdf/2510.10518.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10518v3" onclick="toggleFavorite(this, '2510.10518v3', 'VR-Thinker: Boosting Video Reward Models through Thinking-with-Image Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qunzhong Wang, Jie Liu, Jiajun Liang, Yilei Jiang, Yuanxing Zhang, Jinyuan Chen, Yaozhi Zheng, Xintao Wang, Pengfei Wan, Xiangyu Yue, Jiaheng Liu

**分类**: cs.CV

**发布日期**: 2025-10-12 (更新: 2025-10-15)

---

## 💡 一句话要点

**VR-Thinker：通过图像推理增强视频奖励模型，提升长视频偏好判断。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频奖励模型` `图像推理` `多模态学习` `强化学习` `长视频理解` `视觉记忆` `思维链推理`

## 📋 核心要点

1. 现有视频奖励模型受限于视觉输入的上下文预算，导致无法处理长视频，且容易在推理过程中产生幻觉。
2. VR-Thinker 引入了“图像推理”机制，使模型能够主动选择和更新视觉证据，从而在有限的上下文中进行更可靠的推理。
3. 通过冷启动、拒绝采样微调和组相对策略优化等强化学习方法，VR-Thinker在多个视频偏好基准测试中取得了SOTA结果。

## 📝 摘要（中文）

多模态奖励模型(RMs)的最新进展显著改善了视觉生成模型的后训练。然而，当前的RMs面临固有的局限性：(1)视觉输入消耗大量的上下文预算，迫使减少帧数，导致丢失细粒度细节；(2)所有视觉信息都被打包到初始提示中，加剧了思维链推理过程中的幻觉和遗忘。为了克服这些问题，我们引入了VideoReward Thinker (VR-Thinker)，这是一个通过图像推理的框架，它为RM配备了视觉推理操作(例如，选择帧)和一个可配置的视觉记忆窗口。这使得RM能够在上下文限制内主动获取和更新视觉证据，提高推理的保真度和可靠性。我们通过强化微调管道激活视觉推理：(i)使用精选的视觉思维链数据进行冷启动，以提炼基本的推理技能和操作格式；(ii)选择每个维度和总体判断都正确的样本，然后对这些高质量的轨迹进行拒绝采样微调，以进一步增强推理；(iii)应用组相对策略优化(GRPO)来加强推理。我们的方法在视频偏好基准测试中提供了最先进的准确性，尤其是在较长的视频中：一个7B VR-Thinker在VideoGen Reward上达到80.5%，在GenAI-Bench上达到82.3%，在MJ-Bench-Video上达到75.6%。这些结果验证了通过图像进行多模态奖励建模的有效性和前景。

## 🔬 方法详解

**问题定义**：现有视频奖励模型在处理长视频时，由于视觉信息量大，上下文预算有限，导致模型无法充分利用所有帧的信息，容易丢失细节，并且在思维链推理过程中出现幻觉和遗忘现象。这限制了模型对视频内容进行准确和可靠评估的能力。

**核心思路**：VR-Thinker的核心思路是赋予奖励模型“思考”的能力，使其能够像人类一样，主动选择和利用关键的视觉信息进行推理。通过引入视觉推理操作和视觉记忆窗口，模型可以在有限的上下文预算下，动态地获取和更新视觉证据，从而提高推理的准确性和可靠性。

**技术框架**：VR-Thinker的整体框架包含以下几个主要模块：1) 视觉推理模块：负责执行视觉推理操作，例如选择关键帧。2) 视觉记忆窗口：用于存储和更新视觉证据。3) 奖励模型：基于视觉证据进行奖励预测。训练过程包括：(1) 冷启动：使用精选的视觉思维链数据进行预训练，学习基本的推理技能和操作格式。(2) 拒绝采样微调：选择高质量的推理轨迹进行微调，进一步增强推理能力。(3) 组相对策略优化：使用GRPO算法优化策略，提高推理的鲁棒性。

**关键创新**：VR-Thinker的关键创新在于提出了“通过图像推理”的多模态奖励建模方法。与传统的将所有视觉信息打包到初始提示中的方法不同，VR-Thinker允许模型主动地与视觉信息进行交互，选择和利用关键信息进行推理。这种方法更符合人类的认知过程，能够有效地提高推理的准确性和可靠性。

**关键设计**：VR-Thinker的关键设计包括：(1) 可配置的视觉记忆窗口大小，用于控制模型可以存储的视觉证据数量。(2) 基于强化学习的训练pipeline，包括冷启动、拒绝采样微调和组相对策略优化，用于有效地训练视觉推理模块。(3) 视觉推理操作的具体实现，例如使用注意力机制选择关键帧。

## 📊 实验亮点

VR-Thinker在多个视频偏好基准测试中取得了显著的性能提升。例如，一个7B参数的VR-Thinker模型在VideoGen Reward上达到了80.5%的准确率，在GenAI-Bench上达到了82.3%的准确率，在MJ-Bench-Video上达到了75.6%的准确率。这些结果表明，VR-Thinker在长视频偏好判断方面具有显著优势。

## 🎯 应用场景

VR-Thinker可应用于视频生成模型的训练和评估，例如通过奖励模型引导生成更高质量、更符合人类偏好的视频内容。此外，该技术还可用于视频内容理解、视频摘要、视频质量评估等领域，具有广泛的应用前景。

## 📄 摘要（原文）

> Recent advancements in multimodal reward models (RMs) have substantially improved post-training for visual generative models. However, current RMs face inherent limitations: (1) visual inputs consume large context budgets, forcing fewer frames and causing loss of fine-grained details; and (2) all visual information is packed into the initial prompt, exacerbating hallucination and forgetting during chain-of-thought reasoning. To overcome these issues, we introduce VideoReward Thinker (VR-Thinker), a thinking-with-image framework that equips the RM with visual reasoning operations (e.g., select frame) and a configurable visual memory window. This allows the RM to actively acquire and update visual evidence within context limits, improving reasoning fidelity and reliability. We activate visual reasoning via a reinforcement fine-tuning pipeline: (i) Cold Start with curated visual chain-of-thought data to distill basic reasoning skills and operation formatting; (ii) select samples whose per-dimension and overall judgments are all correct, then conduct Rejection sampling Fine-Tuning on these high-quality traces to further enhance reasoning; and (iii) apply Group Relative Policy Optimization (GRPO) to strengthen reasoning. Our approach delivers state-of-the-art accuracy among open-source models on video preference benchmarks, especially for longer videos: a 7B VR-Thinker achieves 80.5% on VideoGen Reward, 82.3% on GenAI-Bench, and 75.6% on MJ-Bench-Video. These results validate the effectiveness and promise of thinking-with-image multimodal reward modeling.

