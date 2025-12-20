---
layout: default
title: AdaTooler-V: Adaptive Tool-Use for Images and Videos
---

# AdaTooler-V: Adaptive Tool-Use for Images and Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16918" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16918v1</a>
  <a href="https://arxiv.org/pdf/2512.16918.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16918v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16918v1', 'AdaTooler-V: Adaptive Tool-Use for Images and Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chaoyang Wang, Kaituo Feng, Dongyang Chen, Zhongyu Wang, Zhixun Li, Sicheng Gao, Meng Meng, Xu Zhou, Manyuan Zhang, Yuzhang Shang, Xiangyu Yue

**分类**: cs.CV

**发布日期**: 2025-12-18

**备注**: Project page: https://github.com/CYWang735/AdaTooler-V

---

## 💡 一句话要点

**AdaTooler-V：一种自适应工具使用的图像和视频多模态大语言模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `自适应工具使用` `强化学习` `视觉推理` `图像理解`

## 📋 核心要点

1. 现有开源多模态大语言模型存在盲目工具使用模式，即使不必要也会调用视觉工具，显著增加推理开销并降低模型性能。
2. AdaTooler-V通过判断视觉问题是否真正需要工具，从而实现自适应工具使用，避免不必要的工具调用。
3. 实验结果表明，AdaTooler-V在多个视觉推理任务中超越现有方法，并在高分辨率基准测试中超过GPT-4o和Gemini 1.5 Pro。

## 📝 摘要（中文）

本文提出AdaTooler-V，一种多模态大语言模型(MLLM)，通过确定视觉问题是否真正需要工具来执行自适应工具使用。为了实现这一目标，我们引入了AT-GRPO，一种强化学习算法，它基于每个样本的工具效益评分自适应地调整奖励尺度，鼓励模型仅在工具提供真正改进时才调用它们。此外，我们构建了两个数据集来支持训练：AdaTooler-V-CoT-100k用于SFT冷启动，AdaTooler-V-300k用于RL，具有跨单图像、多图像和视频数据的可验证奖励。在十二个基准测试上的实验表明了AdaTooler-V强大的推理能力，在各种视觉推理任务中优于现有方法。值得注意的是，AdaTooler-V-7B在高分辨率基准V*上实现了89.8%的准确率，超过了商业专有模型GPT-4o和Gemini 1.5 Pro。所有代码、模型和数据均已发布。

## 🔬 方法详解

**问题定义**：现有开源多模态大语言模型在处理视觉任务时，常常不加区分地调用视觉工具，即使这些工具对于解决问题并非必要。这种盲目使用工具的方式导致了计算资源的浪费，增加了推理时间，并且在某些情况下还会降低模型的性能，因为不相关的工具可能会引入噪声或干扰。

**核心思路**：AdaTooler-V的核心思路是让模型具备自适应地判断是否需要使用工具的能力。模型需要学习何时应该调用工具以提升性能，以及何时应该避免调用工具以节省计算资源。这种自适应性是通过强化学习来实现的，模型根据其行为获得的奖励来学习最佳的工具使用策略。

**技术框架**：AdaTooler-V的整体框架包括预训练的多模态大语言模型、工具调用模块和强化学习训练模块。首先，使用AdaTooler-V-CoT-100k数据集进行监督微调(SFT)，使模型具备初步的工具使用能力。然后，使用AdaTooler-V-300k数据集，通过AT-GRPO强化学习算法对模型进行训练，使其能够自适应地选择是否调用工具。AT-GRPO算法根据每个样本的工具效益评分来调整奖励尺度，鼓励模型仅在工具能够带来显著改进时才调用它们。

**关键创新**：AdaTooler-V的关键创新在于AT-GRPO强化学习算法和自适应工具使用策略。AT-GRPO算法能够根据样本的特性动态调整奖励，从而更有效地训练模型。自适应工具使用策略使得模型能够根据具体任务的需求，智能地选择是否调用工具，避免了盲目使用工具带来的问题。此外，构建的两个数据集AdaTooler-V-CoT-100k和AdaTooler-V-300k也为模型的训练提供了高质量的数据支持。

**关键设计**：AT-GRPO算法的关键设计在于工具效益评分(Tool Benefit Score)的计算方式和奖励尺度的调整策略。工具效益评分用于衡量工具的使用对解决问题带来的提升程度。奖励尺度根据工具效益评分进行调整，当工具效益评分较高时，模型调用工具会获得更高的奖励；当工具效益评分较低时，模型调用工具会受到惩罚。这种设计鼓励模型学习仅在工具能够带来显著改进时才调用它们。具体的奖励函数和网络结构等细节在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16918v1/x3.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16918v1/x4.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16918v1/x5.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

AdaTooler-V在十二个基准测试中表现出色，证明了其强大的推理能力。尤其是在高分辨率基准V*上，AdaTooler-V-7B实现了89.8%的准确率，超过了商业专有模型GPT-4o和Gemini 1.5 Pro。这表明AdaTooler-V在处理复杂视觉任务方面具有显著优势，并且能够与最先进的商业模型相媲美。

## 🎯 应用场景

AdaTooler-V在多个领域具有广泛的应用前景，例如智能客服、自动驾驶、医疗诊断等。它可以用于处理各种视觉推理任务，例如图像描述、视觉问答、视频理解等。通过自适应地选择是否调用工具，AdaTooler-V可以提高推理效率，降低计算成本，并提升模型性能。未来，该技术有望应用于更复杂的视觉任务，并与其他技术相结合，实现更智能化的视觉系统。

## 📄 摘要（原文）

> Recent advances have shown that multimodal large language models (MLLMs) benefit from multimodal interleaved chain-of-thought (CoT) with vision tool interactions. However, existing open-source models often exhibit blind tool-use reasoning patterns, invoking vision tools even when they are unnecessary, which significantly increases inference overhead and degrades model performance. To this end, we propose AdaTooler-V, an MLLM that performs adaptive tool-use by determining whether a visual problem truly requires tools. First, we introduce AT-GRPO, a reinforcement learning algorithm that adaptively adjusts reward scales based on the Tool Benefit Score of each sample, encouraging the model to invoke tools only when they provide genuine improvements. Moreover, we construct two datasets to support training: AdaTooler-V-CoT-100k for SFT cold start and AdaTooler-V-300k for RL with verifiable rewards across single-image, multi-image, and video data. Experiments across twelve benchmarks demonstrate the strong reasoning capability of AdaTooler-V, outperforming existing methods in diverse visual reasoning tasks. Notably, AdaTooler-V-7B achieves an accuracy of 89.8\% on the high-resolution benchmark V*, surpassing the commercial proprietary model GPT-4o and Gemini 1.5 Pro. All code, models, and data are released.

