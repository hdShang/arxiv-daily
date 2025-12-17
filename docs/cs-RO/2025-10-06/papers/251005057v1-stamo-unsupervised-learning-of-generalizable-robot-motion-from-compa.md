---
layout: default
title: StaMo: Unsupervised Learning of Generalizable Robot Motion from Compact State Representation
---

# StaMo: Unsupervised Learning of Generalizable Robot Motion from Compact State Representation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.05057" target="_blank" class="toolbar-btn">arXiv: 2510.05057v1</a>
    <a href="https://arxiv.org/pdf/2510.05057.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.05057v1" 
            onclick="toggleFavorite(this, '2510.05057v1', 'StaMo: Unsupervised Learning of Generalizable Robot Motion from Compact State Representation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Mingyu Liu, Jiuhe Shu, Hui Chen, Zeju Li, Canyu Zhao, Jiange Yang, Shenyuan Gao, Hao Chen, Chunhua Shen

**分类**: cs.RO, cs.CV

**发布日期**: 2025-10-06

---

## 💡 一句话要点

**StaMo：基于紧凑状态表征无监督学习通用机器人运动**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人运动学习` `状态表征` `无监督学习` `扩散Transformer` `潜在动作` `具身智能` `策略协同训练`

## 📋 核心要点

1. 现有机器人学习方法难以在状态表征的表达性和紧凑性之间取得平衡，限制了世界建模和决策效率。
2. StaMo利用轻量级编码器和预训练的扩散Transformer，学习高度压缩的双token状态表征，并从中提取潜在动作。
3. 实验表明，StaMo在LIBERO和真实世界任务中显著提升性能，并能有效扩展到不同数据源。

## 📝 摘要（中文）

具身智能的一个根本挑战是开发富有表现力且紧凑的状态表征，以实现高效的世界建模和决策。然而，现有方法通常无法实现这种平衡，导致表征要么过于冗余，要么缺乏任务关键信息。我们提出了一种无监督方法，该方法使用轻量级编码器和预训练的扩散Transformer (DiT) 解码器学习高度压缩的双token状态表征，利用其强大的生成先验。我们的表征是高效的、可解释的，并且可以无缝集成到现有的基于VLA的模型中，在LIBERO上提高了14.3%的性能，在真实世界任务成功率上提高了30%，且推理开销最小。更重要的是，我们发现这些token之间的差异，通过潜在插值获得，自然地充当了一种高效的潜在动作，可以进一步解码为可执行的机器人动作。这种涌现的能力表明，我们的表征在没有显式监督的情况下捕获了结构化的动力学。我们将我们的方法命名为StaMo，因为它能够从静态图像编码的紧凑状态表征中学习通用的机器人运动，挑战了对复杂架构和视频数据学习潜在动作的普遍依赖。由此产生的潜在动作也增强了策略协同训练，优于先前的方法10.4%，并提高了可解释性。此外，我们的方法可以有效地扩展到不同的数据源，包括真实世界的机器人数据、模拟和人类自我中心视频。

## 🔬 方法详解

**问题定义**：现有机器人学习方法在状态表征方面存在不足，要么过于冗余，要么缺乏关键信息，难以实现高效的世界建模和决策。现有方法依赖复杂架构和视频数据学习潜在动作，计算成本高昂，泛化能力有限。

**核心思路**：StaMo的核心思想是利用预训练的扩散Transformer (DiT) 的强大生成先验，学习一种高度压缩的双token状态表征。通过对这两个token进行潜在插值，提取出潜在动作，从而在没有显式监督的情况下捕获结构化的动力学。这种方法旨在从静态图像中学习通用的机器人运动，降低对复杂架构和视频数据的依赖。

**技术框架**：StaMo包含一个轻量级编码器和一个预训练的扩散Transformer (DiT) 解码器。编码器将静态图像编码为两个token的状态表征。然后，通过对这两个token进行潜在插值，得到潜在动作。最后，解码器将潜在动作解码为可执行的机器人动作。整个框架是无监督学习的，不需要显式的动作标签。

**关键创新**：StaMo的关键创新在于其双token状态表征和潜在动作提取方法。通过学习两个token的差异，StaMo能够捕获状态之间的动态变化，从而提取出有效的潜在动作。这种方法避免了对复杂架构和视频数据的依赖，降低了计算成本，提高了泛化能力。此外，利用预训练的扩散Transformer (DiT) 的强大生成先验也是一个重要的创新点。

**关键设计**：StaMo的关键设计包括：1) 轻量级编码器的选择，以保证计算效率；2) 预训练的扩散Transformer (DiT) 的使用，以提供强大的生成先验；3) 双token状态表征的设计，以便提取潜在动作；4) 潜在插值方法的选择，以保证潜在动作的有效性。具体的参数设置和网络结构细节在论文中进行了详细描述（未知）。损失函数的设计目标是最小化重构误差，并鼓励学习到的状态表征具有良好的可解释性和泛化能力（未知）。

## 📊 实验亮点

StaMo在LIBERO数据集上性能提升14.3%，在真实世界任务成功率上提升30%，且推理开销极小。与现有方法相比，StaMo在策略协同训练中性能提升10.4%，并提高了可解释性。此外，StaMo能够有效扩展到不同的数据源，包括真实世界的机器人数据、模拟和人类自我中心视频。

## 🎯 应用场景

StaMo具有广泛的应用前景，可用于机器人控制、自动驾驶、游戏AI等领域。通过学习通用的机器人运动，StaMo可以帮助机器人更好地理解环境，做出更合理的决策。此外，StaMo还可以用于生成逼真的机器人动画，提高用户体验。未来，StaMo有望成为具身智能领域的重要技术。

## 📄 摘要（原文）

> A fundamental challenge in embodied intelligence is developing expressive and compact state representations for efficient world modeling and decision making. However, existing methods often fail to achieve this balance, yielding representations that are either overly redundant or lacking in task-critical information. We propose an unsupervised approach that learns a highly compressed two-token state representation using a lightweight encoder and a pre-trained Diffusion Transformer (DiT) decoder, capitalizing on its strong generative prior. Our representation is efficient, interpretable, and integrates seamlessly into existing VLA-based models, improving performance by 14.3% on LIBERO and 30% in real-world task success with minimal inference overhead. More importantly, we find that the difference between these tokens, obtained via latent interpolation, naturally serves as a highly effective latent action, which can be further decoded into executable robot actions. This emergent capability reveals that our representation captures structured dynamics without explicit supervision. We name our method StaMo for its ability to learn generalizable robotic Motion from compact State representation, which is encoded from static images, challenging the prevalent dependence to learning latent action on complex architectures and video data. The resulting latent actions also enhance policy co-training, outperforming prior methods by 10.4% with improved interpretability. Moreover, our approach scales effectively across diverse data sources, including real-world robot data, simulation, and human egocentric video.

