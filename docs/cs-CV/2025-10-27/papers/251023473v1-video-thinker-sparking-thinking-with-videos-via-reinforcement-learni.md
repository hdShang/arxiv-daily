---
layout: default
title: Video-Thinker: Sparking "Thinking with Videos" via Reinforcement Learning
---

# Video-Thinker: Sparking "Thinking with Videos" via Reinforcement Learning

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.23473" target="_blank" class="toolbar-btn">arXiv: 2510.23473v1</a>
    <a href="https://arxiv.org/pdf/2510.23473.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23473v1" 
            onclick="toggleFavorite(this, '2510.23473v1', 'Video-Thinker: Sparking \"Thinking with Videos\" via Reinforcement Learning')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Shijian Wang, Jiarui Jin, Xingjian Wang, Linxin Song, Runhao Fu, Hecheng Wang, Zongyuan Ge, Yuan Lu, Xuelian Cheng

**分类**: cs.CV

**发布日期**: 2025-10-27

---

## 💡 一句话要点

**提出Video-Thinker，通过强化学习赋能MLLM进行视频推理**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频推理` `多模态大语言模型` `强化学习` `思维链` `自主推理` `视频理解` `定位` `描述`

## 📋 核心要点

1. 现有方法缺乏动态推理能力，无法有效利用视频信息进行复杂推理。
2. Video-Thinker利用MLLM自身能力，通过强化学习自主生成推理线索，无需外部工具。
3. 实验表明，Video-Thinker在多个视频推理基准测试中显著优于现有方法，达到SOTA。

## 📝 摘要（中文）

本文提出Video-Thinker，旨在通过强化学习赋能多模态大型语言模型（MLLM）进行视频推理，使其能够自主利用其内在的“定位”和“描述”能力，在推理过程中生成推理线索。为了激发这种能力，我们构建了一个名为Video-Thinker-10K的数据集，该数据集包含在思维链推理序列中自主工具使用的示例。我们的训练策略首先使用监督微调（SFT）来学习推理格式，然后使用组相对策略优化（GRPO）来加强这种推理能力。通过这种方法，Video-Thinker使MLLM能够自主地进行视频推理的定位和描述任务，而无需构建和调用外部工具。大量实验表明，Video-Thinker在领域内任务和具有挑战性的领域外视频推理基准（包括Video-Holmes、CG-Bench-Reasoning和VRBench）上都取得了显著的性能提升。我们的Video-Thinker-7B显著优于现有的基线模型（如Video-R1），并在7B大小的MLLM中建立了最先进的性能。

## 🔬 方法详解

**问题定义**：现有的多模态大型语言模型在图像推理方面取得了显著进展，但缺乏对视频进行动态推理的能力。它们难以有效地利用视频中的时序信息和动态变化，从而限制了其在复杂视频理解任务中的应用。现有方法通常依赖于预定义的外部工具或模块，缺乏自主性和灵活性。

**核心思路**：Video-Thinker的核心思路是赋予MLLM自主“思考”视频的能力，使其能够像人类一样，通过观察和分析视频内容，逐步生成推理线索，最终完成推理任务。这种方法避免了对外部工具的依赖，充分利用了MLLM自身所具备的“定位”和“描述”能力。

**技术框架**：Video-Thinker的整体框架包括以下几个主要阶段：首先，使用监督微调（SFT）在Video-Thinker-10K数据集上训练MLLM，使其学习视频推理的基本格式和流程。然后，使用组相对策略优化（GRPO）进一步提升MLLM的推理能力，使其能够更好地利用视频信息生成有效的推理线索。在推理过程中，MLLM自主地进行定位和描述任务，生成中间推理步骤，最终得到推理结果。

**关键创新**：Video-Thinker最重要的技术创新点在于其自主推理的模式。与传统方法不同，Video-Thinker不依赖于预定义的外部工具或模块，而是通过强化学习赋予MLLM自主生成推理线索的能力。这种方法使得MLLM能够更加灵活地适应不同的视频推理任务，并能够更好地利用视频中的动态信息。

**关键设计**：Video-Thinker的关键设计包括：1) Video-Thinker-10K数据集，该数据集包含在思维链推理序列中自主工具使用的示例，用于训练MLLM的推理能力；2) 组相对策略优化（GRPO），用于进一步提升MLLM的推理能力，使其能够更好地利用视频信息生成有效的推理线索；3) 自主定位和描述任务，MLLM在推理过程中自主地进行定位和描述任务，生成中间推理步骤，最终得到推理结果。

## 📊 实验亮点

Video-Thinker-7B在多个视频推理基准测试中取得了显著的性能提升，例如在Video-Holmes上，Video-Thinker-7B的性能显著优于现有的基线模型（如Video-R1），并在7B大小的MLLM中建立了最先进的性能。在CG-Bench-Reasoning和VRBench等其他基准测试中，Video-Thinker也表现出了优异的性能。

## 🎯 应用场景

Video-Thinker具有广泛的应用前景，例如智能监控、视频内容分析、自动驾驶、机器人导航等领域。它可以用于识别异常行为、理解视频内容、辅助驾驶决策、以及指导机器人完成复杂任务。通过赋予机器自主思考视频的能力，Video-Thinker有望推动人工智能技术在视频理解领域的进一步发展。

## 📄 摘要（原文）

> Recent advances in image reasoning methods, particularly "Thinking with Images", have demonstrated remarkable success in Multimodal Large Language Models (MLLMs); however, this dynamic reasoning paradigm has not yet been extended to video reasoning tasks. In this paper, we propose Video-Thinker, which empowers MLLMs to think with videos by autonomously leveraging their intrinsic "grounding" and "captioning" capabilities to generate reasoning clues throughout the inference process. To spark this capability, we construct Video-Thinker-10K, a curated dataset featuring autonomous tool usage within chain-of-thought reasoning sequences. Our training strategy begins with Supervised Fine-Tuning (SFT) to learn the reasoning format, followed by Group Relative Policy Optimization (GRPO) to strengthen this reasoning capability. Through this approach, Video-Thinker enables MLLMs to autonomously navigate grounding and captioning tasks for video reasoning, eliminating the need for constructing and calling external tools. Extensive experiments demonstrate that Video-Thinker achieves significant performance gains on both in-domain tasks and challenging out-of-domain video reasoning benchmarks, including Video-Holmes, CG-Bench-Reasoning, and VRBench. Our Video-Thinker-7B substantially outperforms existing baselines such as Video-R1 and establishes state-of-the-art performance among 7B-sized MLLMs.

