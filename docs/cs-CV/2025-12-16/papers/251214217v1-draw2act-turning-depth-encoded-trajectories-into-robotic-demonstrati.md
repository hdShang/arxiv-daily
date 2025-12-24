---
layout: default
title: "DRAW2ACT: Turning Depth-Encoded Trajectories into Robotic Demonstration Videos"
---

# DRAW2ACT: Turning Depth-Encoded Trajectories into Robotic Demonstration Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14217" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14217v1</a>
  <a href="https://arxiv.org/pdf/2512.14217.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14217v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14217v1', 'DRAW2ACT: Turning Depth-Encoded Trajectories into Robotic Demonstration Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yang Bai, Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Ziyuan Liu, Gitta Kutyniok

**分类**: cs.CV, cs.RO

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**DRAW2ACT：提出深度感知的轨迹条件视频生成框架，用于机器人操作演示视频生成。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频生成` `机器人操作` `轨迹条件` `深度感知` `扩散模型`

## 📋 核心要点

1. 现有轨迹条件视频生成方法依赖2D轨迹或单模态信息，限制了机器人演示视频的可控性和一致性。
2. DRAW2ACT提取轨迹的深度、语义、形状和运动等多重表示，并融入扩散模型，实现深度感知的视频生成。
3. 实验表明，DRAW2ACT在视觉保真度、一致性和操作成功率方面优于现有方法，提升了机器人操作性能。

## 📝 摘要（中文）

视频扩散模型为具身智能提供了强大的真实世界模拟器，但在机器人操作的可控性方面仍然有限。最近关于轨迹条件视频生成的工作弥补了这一差距，但通常依赖于2D轨迹或单模态条件，这限制了它们生成可控且一致的机器人演示的能力。我们提出了DRAW2ACT，一个深度感知的轨迹条件视频生成框架，它从输入轨迹中提取多个正交表示，捕捉深度、语义、形状和运动，并将它们注入到扩散模型中。此外，我们提出联合生成空间对齐的RGB和深度视频，利用跨模态注意力机制和深度监督来增强时空一致性。最后，我们引入了一个以生成的RGB和深度序列为条件的多模态策略模型来回归机器人的关节角度。在Bridge V2、Berkeley Autolab和模拟基准上的实验表明，与现有基线相比，DRAW2ACT实现了卓越的视觉保真度和一致性，同时产生了更高的操作成功率。

## 🔬 方法详解

**问题定义**：现有的轨迹条件视频生成方法在机器人操作领域存在局限性，主要体现在对轨迹信息的利用不足，通常只依赖于2D轨迹或单一模态的条件信息，导致生成的视频在可控性和一致性方面表现不佳。这些方法难以准确捕捉机器人操作过程中的深度信息、语义信息、形状变化和运动轨迹，从而限制了生成高质量机器人演示视频的能力。

**核心思路**：DRAW2ACT的核心思路是从输入轨迹中提取更丰富的表示，包括深度、语义、形状和运动信息，并将这些信息有效地融入到视频扩散模型中。通过这种方式，模型可以更好地理解和模拟机器人操作过程，从而生成更逼真、可控和一致的视频。同时，联合生成RGB和深度视频，利用跨模态信息增强时空一致性。

**技术框架**：DRAW2ACT框架主要包含轨迹表示提取模块、视频生成模块和策略模型模块。轨迹表示提取模块负责从输入轨迹中提取深度、语义、形状和运动等多种表示。视频生成模块利用扩散模型，以提取的轨迹表示为条件，生成RGB和深度视频。该模块采用跨模态注意力机制和深度监督来增强RGB和深度视频的时空一致性。策略模型模块则以生成的RGB和深度序列为条件，回归机器人的关节角度，实现机器人控制。

**关键创新**：DRAW2ACT的关键创新在于深度感知的轨迹条件视频生成方法。它通过提取轨迹的多种正交表示，并将其注入到扩散模型中，实现了对机器人操作过程更全面的建模。与现有方法相比，DRAW2ACT能够更好地捕捉机器人操作的细节和复杂性，从而生成更高质量的视频。此外，联合生成RGB和深度视频并利用跨模态信息也增强了视频的时空一致性。

**关键设计**：DRAW2ACT在视频生成模块中使用了跨模态注意力机制，允许RGB和深度信息相互影响，从而增强时空一致性。此外，还采用了深度监督，通过引入额外的深度损失来约束生成的深度视频的质量。在网络结构方面，DRAW2ACT采用了标准的扩散模型架构，并针对轨迹条件进行了修改，以更好地融合轨迹信息。具体的参数设置和损失函数选择需要根据具体的实验数据进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14217v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14217v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14217v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

DRAW2ACT在Bridge V2、Berkeley Autolab和模拟基准上进行了实验，结果表明，与现有基线相比，DRAW2ACT在视觉保真度和一致性方面取得了显著提升，同时操作成功率也更高。具体的数据指标和提升幅度在论文中进行了详细的展示和分析，证明了DRAW2ACT的有效性和优越性。

## 🎯 应用场景

DRAW2ACT具有广泛的应用前景，可用于机器人技能学习、机器人操作演示、虚拟环境生成和增强现实等领域。通过生成高质量的机器人操作视频，可以帮助机器人更好地理解和学习人类的技能，提高机器人的自主操作能力。此外，该技术还可以用于创建逼真的虚拟环境，用于机器人训练和测试，降低实际实验的成本和风险。

## 📄 摘要（原文）

> Video diffusion models provide powerful real-world simulators for embodied AI but remain limited in controllability for robotic manipulation. Recent works on trajectory-conditioned video generation address this gap but often rely on 2D trajectories or single modality conditioning, which restricts their ability to produce controllable and consistent robotic demonstrations. We present DRAW2ACT, a depth-aware trajectory-conditioned video generation framework that extracts multiple orthogonal representations from the input trajectory, capturing depth, semantics, shape and motion, and injects them into the diffusion model. Moreover, we propose to jointly generate spatially aligned RGB and depth videos, leveraging cross-modality attention mechanisms and depth supervision to enhance the spatio-temporal consistency. Finally, we introduce a multimodal policy model conditioned on the generated RGB and depth sequences to regress the robot's joint angles. Experiments on Bridge V2, Berkeley Autolab, and simulation benchmarks show that DRAW2ACT achieves superior visual fidelity and consistency while yielding higher manipulation success rates compared to existing baselines.

