---
layout: default
title: "EmbodiedSplat: Personalized Real-to-Sim-to-Real Navigation with Gaussian Splats from a Mobile Device"
---

# EmbodiedSplat: Personalized Real-to-Sim-to-Real Navigation with Gaussian Splats from a Mobile Device

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.17430" class="toolbar-btn" target="_blank">📄 arXiv: 2509.17430v2</a>
  <a href="https://arxiv.org/pdf/2509.17430.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.17430v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.17430v2', 'EmbodiedSplat: Personalized Real-to-Sim-to-Real Navigation with Gaussian Splats from a Mobile Device')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gunjan Chhablani, Xiaomeng Ye, Muhammad Zubair Irshad, Zsolt Kira

**分类**: cs.CV, cs.RO

**发布日期**: 2025-09-22 (更新: 2025-09-23)

**备注**: 16 pages, 18 figures, paper accepted at ICCV, 2025

**🔗 代码/项目**: [PROJECT_PAGE](https://gchhablani.github.io/embodied-splat)

---

## 💡 一句话要点

**EmbodiedSplat：利用高斯溅射和移动设备实现个性化的实-仿-实导航**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能` `Sim-to-Real` `3D高斯溅射` `移动设备` `导航策略` `Habitat-Sim` `场景重建`

## 📋 核心要点

1. 现有Embodied AI方法依赖仿真，但合成环境缺乏真实感，真实重建成本高昂，导致sim-to-real迁移困难。
2. EmbodiedSplat利用iPhone捕获环境，通过3D高斯溅射重建场景，并在Habitat-Sim中微调策略，实现个性化训练。
3. 实验表明，EmbodiedSplat在真实图像导航任务上，相比zero-shot基线，成功率提升高达20%-40%，sim-vs-real相关性高达0.87-0.97。

## 📝 摘要（中文）

Embodied AI领域主要依赖于仿真进行训练和评估，但常用的全合成环境缺乏真实感，而高保真真实世界重建则需要昂贵的硬件。这导致了从仿真到真实的迁移仍然是一个主要挑战。本文提出了EmbodiedSplat，一种新颖的方法，通过高效地捕获部署环境并在重建的场景中微调策略来个性化策略训练。我们的方法利用3D高斯溅射(GS)和Habitat-Sim模拟器来弥合真实场景捕获和有效训练环境之间的差距。使用iPhone捕获的部署场景，我们通过GS重建网格，从而能够在接近真实世界条件的设置中进行训练。我们对训练策略、预训练数据集和网格重建技术进行了全面分析，评估了它们对真实世界场景中sim-to-real预测性的影响。实验结果表明，使用EmbodiedSplat微调的智能体优于在大型真实世界数据集(HM3D)和合成生成数据集(HSSD)上预训练的zero-shot基线，在真实世界图像导航任务上实现了20%和40%的绝对成功率提升。此外，我们的方法为重建的网格产生了高的sim-vs-real相关性(0.87-0.97)，突出了其在以最小的努力适应多样化环境方面的有效性。

## 🔬 方法详解

**问题定义**：Embodied AI中的sim-to-real迁移问题，即在仿真环境中训练的智能体难以直接应用于真实世界。现有方法要么使用不真实的合成环境，要么依赖昂贵的硬件进行真实场景重建，无法兼顾训练效率和真实性。

**核心思路**：利用移动设备（如iPhone）快速捕获真实环境，通过3D高斯溅射（3D Gaussian Splatting, GS）技术重建场景，然后在Habitat-Sim模拟器中进行策略微调。这种方法旨在创建一个更真实的训练环境，从而提高sim-to-real的迁移能力。

**技术框架**：整体流程包括：1) 使用iPhone等移动设备捕获真实环境的图像；2) 利用3D高斯溅射技术从图像中重建场景的3D网格；3) 将重建的网格导入Habitat-Sim模拟器；4) 在模拟器中训练或微调导航策略；5) 在真实环境中部署训练好的智能体。

**关键创新**：EmbodiedSplat的关键创新在于将3D高斯溅射技术应用于Embodied AI的sim-to-real迁移问题。与传统的基于mesh的重建方法相比，高斯溅射能够更高效、更准确地重建场景，并且更容易与现有的模拟器集成。此外，该方法利用移动设备进行场景捕获，降低了数据采集的成本和门槛。

**关键设计**：论文详细分析了不同的训练策略（如从头训练或微调）、预训练数据集（如HM3D和HSSD）以及网格重建技术对sim-to-real性能的影响。具体的技术细节包括：高斯溅射的参数设置、Habitat-Sim模拟器的配置、导航策略的网络结构和损失函数等。论文还探讨了如何优化这些参数，以获得最佳的sim-to-real迁移效果。

## 📊 实验亮点

实验结果表明，使用EmbodiedSplat微调的智能体在真实世界图像导航任务上取得了显著的性能提升。相比于在大型真实世界数据集（HM3D）上预训练的zero-shot基线，成功率提升了20%；相比于在合成生成数据集（HSSD）上预训练的zero-shot基线，成功率提升了40%。此外，重建的网格具有很高的sim-vs-real相关性（0.87-0.97），验证了该方法在创建真实训练环境方面的有效性。

## 🎯 应用场景

EmbodiedSplat具有广泛的应用前景，例如家庭机器人、自动驾驶、增强现实等。它可以帮助机器人更好地理解和适应真实世界环境，从而实现更智能、更自主的导航和交互。该方法降低了数据采集成本，使得个性化机器人训练成为可能，有望加速Embodied AI技术在各行业的落地。

## 📄 摘要（原文）

> The field of Embodied AI predominantly relies on simulation for training and evaluation, often using either fully synthetic environments that lack photorealism or high-fidelity real-world reconstructions captured with expensive hardware. As a result, sim-to-real transfer remains a major challenge. In this paper, we introduce EmbodiedSplat, a novel approach that personalizes policy training by efficiently capturing the deployment environment and fine-tuning policies within the reconstructed scenes. Our method leverages 3D Gaussian Splatting (GS) and the Habitat-Sim simulator to bridge the gap between realistic scene capture and effective training environments. Using iPhone-captured deployment scenes, we reconstruct meshes via GS, enabling training in settings that closely approximate real-world conditions. We conduct a comprehensive analysis of training strategies, pre-training datasets, and mesh reconstruction techniques, evaluating their impact on sim-to-real predictivity in real-world scenarios. Experimental results demonstrate that agents fine-tuned with EmbodiedSplat outperform both zero-shot baselines pre-trained on large-scale real-world datasets (HM3D) and synthetically generated datasets (HSSD), achieving absolute success rate improvements of 20% and 40% on real-world Image Navigation task. Moreover, our approach yields a high sim-vs-real correlation (0.87-0.97) for the reconstructed meshes, underscoring its effectiveness in adapting policies to diverse environments with minimal effort. Project page: https://gchhablani.github.io/embodied-splat.

