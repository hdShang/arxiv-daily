---
layout: default
title: TrackVLA++: Unleashing Reasoning and Memory Capabilities in VLA Models for Embodied Visual Tracking
---

# TrackVLA++: Unleashing Reasoning and Memory Capabilities in VLA Models for Embodied Visual Tracking

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.07134" target="_blank" class="toolbar-btn">arXiv: 2510.07134v1</a>
    <a href="https://arxiv.org/pdf/2510.07134.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07134v1" 
            onclick="toggleFavorite(this, '2510.07134v1', 'TrackVLA++: Unleashing Reasoning and Memory Capabilities in VLA Models for Embodied Visual Tracking')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Jiahang Liu, Yunpeng Qi, Jiazhao Zhang, Minghan Li, Shaoan Wang, Kui Wu, Hanjing Ye, Hong Zhang, Zhibo Chen, Fangwei Zhong, Zhizheng Zhang, He Wang

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-10-08

**备注**: Project page: https://pku-epic.github.io/TrackVLA-plus-plus-Web/

---

## 💡 一句话要点

**TrackVLA++：利用VLA模型中的推理和记忆能力实现具身视觉跟踪**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身视觉跟踪` `视觉-语言-动作模型` `空间推理` `时序记忆` `思维链` `目标识别` `零样本学习`

## 📋 核心要点

1. 现有语言引导的具身视觉跟踪方法缺乏显式的空间推理能力和有效的时序记忆机制，难以应对遮挡和相似干扰。
2. TrackVLA++通过引入空间推理模块Polar-CoT和目标识别记忆模块TIM，增强了模型在复杂场景下的跟踪能力。
3. 实验表明，TrackVLA++在EVT-Bench DT split上显著超越现有方法，并展现出强大的零样本泛化能力。

## 📝 摘要（中文）

具身视觉跟踪(EVT)是伴侣机器人、引导机器人和服务助手等实际应用的基础能力，在这些应用中，持续跟踪移动目标至关重要。最近的进展使得在复杂和非结构化场景中进行语言引导的跟踪成为可能。然而，现有方法缺乏显式的空间推理和有效的时序记忆，导致在严重遮挡或存在相似干扰物时失效。为了应对这些挑战，我们提出了TrackVLA++，一种新型的视觉-语言-动作(VLA)模型，它通过两个关键模块增强了具身视觉跟踪能力：空间推理机制和目标识别记忆(TIM)。推理模块引入了一种思维链范式，称为Polar-CoT，它推断目标的相对位置并将其编码为紧凑的极坐标token用于动作预测。在这些空间先验的指导下，TIM采用门控更新策略来保持长时程目标记忆，确保时空一致性，并减轻在长时间遮挡期间的目标丢失。大量的实验表明，TrackVLA++在自我中心和多摄像头设置下的公共基准测试中都达到了最先进的性能。在具有挑战性的EVT-Bench DT split上，TrackVLA++分别超过了之前的领先方法5.1和12。此外，TrackVLA++表现出强大的零样本泛化能力，能够在动态和遮挡场景中实现鲁棒的真实世界跟踪。

## 🔬 方法详解

**问题定义**：论文旨在解决具身视觉跟踪（EVT）中，现有方法在严重遮挡或存在相似干扰物时，由于缺乏显式的空间推理和有效的时序记忆而导致的跟踪失败问题。现有方法难以维持长时间的目标身份，容易受到环境干扰，鲁棒性较差。

**核心思路**：论文的核心思路是通过引入空间推理机制和目标识别记忆模块，增强模型对目标位置的理解和对目标身份的长期记忆。空间推理模块Polar-CoT用于推断目标的相对位置，并将其编码为极坐标token，为动作预测提供空间先验。目标识别记忆模块TIM则用于保持长时程目标记忆，确保时空一致性，减轻遮挡带来的影响。

**技术框架**：TrackVLA++模型包含视觉、语言和动作三个模态的处理，以及Polar-CoT空间推理模块和TIM目标识别记忆模块。整体流程为：首先，视觉和语言信息被编码成特征表示；然后，Polar-CoT模块根据视觉特征推理目标相对位置，生成极坐标token；接着，TIM模块利用门控更新策略，结合当前视觉特征和历史目标记忆，更新目标表示；最后，基于更新后的目标表示，预测动作。

**关键创新**：论文的关键创新在于Polar-CoT空间推理模块和TIM目标识别记忆模块的引入。Polar-CoT通过思维链的方式，显式地推理目标位置，克服了现有方法缺乏空间推理的不足。TIM通过门控更新策略，有效地保持了长时程目标记忆，提高了模型在遮挡情况下的鲁棒性。

**关键设计**：Polar-CoT模块采用思维链的方式，逐步推理目标位置，并将结果编码为极坐标token。TIM模块采用门控循环单元（GRU）作为记忆单元，并使用门控机制控制信息的更新和遗忘。损失函数包括跟踪损失和辅助损失，用于优化模型参数。

## 📊 实验亮点

TrackVLA++在EVT-Bench DT split上取得了显著的性能提升，超过了之前的领先方法5.1和12。此外，该模型还展现出强大的零样本泛化能力，能够在未见过的动态和遮挡场景中实现鲁棒的跟踪。这些实验结果表明，TrackVLA++在具身视觉跟踪领域具有领先的性能和良好的泛化能力。

## 🎯 应用场景

TrackVLA++在具身视觉跟踪领域具有广泛的应用前景，例如可以应用于伴侣机器人，使其能够可靠地跟随用户；也可以应用于引导机器人，使其能够在复杂环境中引导用户到达目的地；还可以应用于服务助手，使其能够识别并跟踪特定目标，提供个性化服务。该研究的成果有助于提升机器人在真实世界中的交互能力，促进人机协作。

## 📄 摘要（原文）

> Embodied Visual Tracking (EVT) is a fundamental ability that underpins practical applications, such as companion robots, guidance robots and service assistants, where continuously following moving targets is essential. Recent advances have enabled language-guided tracking in complex and unstructured scenes. However, existing approaches lack explicit spatial reasoning and effective temporal memory, causing failures under severe occlusions or in the presence of similar-looking distractors. To address these challenges, we present TrackVLA++, a novel Vision-Language-Action (VLA) model that enhances embodied visual tracking with two key modules, a spatial reasoning mechanism and a Target Identification Memory (TIM). The reasoning module introduces a Chain-of-Thought paradigm, termed Polar-CoT, which infers the target's relative position and encodes it as a compact polar-coordinate token for action prediction. Guided by these spatial priors, the TIM employs a gated update strategy to preserve long-horizon target memory, ensuring spatiotemporal consistency and mitigating target loss during extended occlusions. Extensive experiments show that TrackVLA++ achieves state-of-the-art performance on public benchmarks across both egocentric and multi-camera settings. On the challenging EVT-Bench DT split, TrackVLA++ surpasses the previous leading approach by 5.1 and 12, respectively. Furthermore, TrackVLA++ exhibits strong zero-shot generalization, enabling robust real-world tracking in dynamic and occluded scenarios.

