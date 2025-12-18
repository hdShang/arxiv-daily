---
layout: default
title: VLA-AN: An Efficient and Onboard Vision-Language-Action Framework for Aerial Navigation in Complex Environments
---

# VLA-AN: An Efficient and Onboard Vision-Language-Action Framework for Aerial Navigation in Complex Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15258" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15258v1</a>
  <a href="https://arxiv.org/pdf/2512.15258.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15258v1" onclick="toggleFavorite(this, '2512.15258v1', 'VLA-AN: An Efficient and Onboard Vision-Language-Action Framework for Aerial Navigation in Complex Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuze Wu, Mo Zhu, Xingxing Li, Yuheng Du, Yuxin Fan, Wenjun Li, Xin Zhou, Fei Gao

**分类**: cs.RO, cs.AI

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**提出VLA-AN，用于复杂环境中无人机高效、安全的视觉-语言-动作端到端导航。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言动作` `无人机导航` `3D高斯溅射` `自主导航` `深度学习` `强化学习` `机载部署`

## 📋 核心要点

1. 现有空中导航模型存在数据域差距、时间导航推理不足、生成式动作策略安全风险以及难以在机载部署等问题。
2. VLA-AN通过3D-GS构建高保真数据集，采用渐进式三阶段训练，并设计轻量级安全校正动作模块来解决上述问题。
3. 实验表明，VLA-AN显著提升了空间定位、场景推理和长时程导航能力，并在无人机上实现了8.3倍的推理速度提升。

## 📝 摘要（中文）

本文提出了一种高效的、可用于机载的视觉-语言-动作（VLA）框架VLA-AN，专门用于复杂环境中的无人机自主导航。VLA-AN解决了现有大型空中导航模型的四个主要局限性：数据域差距、推理能力不足的时间导航、生成式动作策略的安全问题以及机载部署约束。首先，我们构建了一个高保真数据集，利用3D高斯溅射（3D-GS）有效地弥合了域差距。其次，我们引入了一个渐进式三阶段训练框架，依次加强场景理解、核心飞行技能和复杂导航能力。第三，我们设计了一个轻量级的、实时的动作模块，并结合了几何安全校正。该模块确保快速、无碰撞和稳定的指令生成，从而减轻了随机生成策略中固有的安全风险。最后，通过对机载部署流程的深度优化，VLA-AN在资源受限的无人机上实现了鲁棒的实时推理吞吐量8.3倍的提升。大量的实验表明，VLA-AN显著提高了空间定位、场景推理和长时程导航能力，实现了高达98.1%的单任务成功率，并为在轻型空中机器人中实现全链闭环自主提供了一种高效、实用的解决方案。

## 🔬 方法详解

**问题定义**：现有的大型空中导航模型在实际应用中面临诸多挑战。首先，仿真数据与真实环境存在显著的域差距，导致模型泛化能力不足。其次，模型在长时间导航中缺乏有效的推理能力，难以应对复杂场景。此外，基于生成式策略的动作控制存在安全隐患，容易导致碰撞。最后，大型模型难以在资源受限的无人机平台上进行实时部署。

**核心思路**：VLA-AN的核心思路是构建一个高效、安全且易于部署的视觉-语言-动作框架，以解决上述问题。通过3D-GS技术生成高保真数据集来缩小域差距，采用渐进式训练策略来提升导航能力，并设计轻量级的动作模块和几何安全校正机制来确保飞行安全。

**技术框架**：VLA-AN框架主要包含三个阶段：1) **数据生成阶段**：利用3D-GS技术构建高保真数据集，模拟真实环境，缩小域差距。2) **训练阶段**：采用渐进式三阶段训练策略，首先训练场景理解能力，然后训练核心飞行技能，最后训练复杂导航能力。3) **部署阶段**：对模型进行优化，使其能够在资源受限的无人机平台上实时运行。

**关键创新**：VLA-AN的关键创新在于：1) 利用3D-GS技术构建高保真数据集，有效弥合了仿真数据与真实环境之间的域差距。2) 提出了渐进式三阶段训练框架，能够有效地提升模型的导航能力。3) 设计了轻量级的动作模块和几何安全校正机制，确保了飞行的安全性。4) 实现了在资源受限的无人机平台上的实时部署。

**关键设计**：在数据生成阶段，使用了高质量的3D-GS模型来渲染逼真的场景图像。在训练阶段，采用了交叉熵损失函数来优化场景理解模块，并使用强化学习算法来训练飞行技能和导航能力。在动作模块中，使用了PID控制器来生成平滑的控制指令，并结合了几何安全校正机制来避免碰撞。模型压缩和优化技术被用于加速推理过程。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15258v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15258v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15258v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，VLA-AN在空间定位、场景推理和长时程导航方面均取得了显著的提升，单任务成功率最高达到98.1%。此外，VLA-AN在资源受限的无人机平台上实现了8.3倍的推理速度提升，验证了其高效性和实用性。这些结果表明，VLA-AN为实现轻型空中机器人的全链闭环自主提供了一种有效的解决方案。

## 🎯 应用场景

VLA-AN框架可广泛应用于无人机自主巡检、物流配送、灾害救援、环境监测等领域。该研究成果有助于提升无人机在复杂环境下的自主导航能力和安全性，降低对人工干预的依赖，具有重要的实际应用价值和广阔的市场前景。

## 📄 摘要（原文）

> This paper proposes VLA-AN, an efficient and onboard Vision-Language-Action (VLA) framework dedicated to autonomous drone navigation in complex environments. VLA-AN addresses four major limitations of existing large aerial navigation models: the data domain gap, insufficient temporal navigation with reasoning, safety issues with generative action policies, and onboard deployment constraints. First, we construct a high-fidelity dataset utilizing 3D Gaussian Splatting (3D-GS) to effectively bridge the domain gap. Second, we introduce a progressive three-stage training framework that sequentially reinforces scene comprehension, core flight skills, and complex navigation capabilities. Third, we design a lightweight, real-time action module coupled with geometric safety correction. This module ensures fast, collision-free, and stable command generation, mitigating the safety risks inherent in stochastic generative policies. Finally, through deep optimization of the onboard deployment pipeline, VLA-AN achieves a robust real-time 8.3x improvement in inference throughput on resource-constrained UAVs. Extensive experiments demonstrate that VLA-AN significantly improves spatial grounding, scene reasoning, and long-horizon navigation, achieving a maximum single-task success rate of 98.1%, and providing an efficient, practical solution for realizing full-chain closed-loop autonomy in lightweight aerial robots.

