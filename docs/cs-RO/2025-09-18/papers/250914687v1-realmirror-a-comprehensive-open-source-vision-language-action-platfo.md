---
layout: default
title: "RealMirror: A Comprehensive, Open-Source Vision-Language-Action Platform for Embodied AI"
---

# RealMirror: A Comprehensive, Open-Source Vision-Language-Action Platform for Embodied AI

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14687" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14687v1</a>
  <a href="https://arxiv.org/pdf/2509.14687.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14687v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14687v1', 'RealMirror: A Comprehensive, Open-Source Vision-Language-Action Platform for Embodied AI')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Cong Tai, Zhaoyu Zheng, Haixu Long, Hansheng Wu, Haodong Xiang, Zhengbin Long, Jun Xiong, Rong Shi, Shizhuang Zhang, Gang Qiu, He Wang, Ruifeng Li, Jun Huang, Bin Chang, Shuai Feng, Tao Shen

**分类**: cs.RO

**发布日期**: 2025-09-18

**🔗 代码/项目**: [PROJECT_PAGE](https://terminators2025.github.io/RealMirror.github.io)

---

## 💡 一句话要点

**RealMirror：为具身AI打造的全面开源视觉-语言-动作平台**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能` `视觉-语言-动作` `人形机器人` `Sim2Real迁移` `开源平台`

## 📋 核心要点

1. 人形机器人VLA研究面临数据获取昂贵、缺乏统一基准、模拟与现实差距大等难题，阻碍了发展。
2. RealMirror平台旨在通过低成本数据收集、模型训练和推理系统，以及专用VLA基准，解决上述问题。
3. 该平台结合生成模型和3D高斯溅射技术，实现了零样本Sim2Real迁移，提升了模型在真实环境中的泛化能力。

## 📝 摘要（中文）

针对人形机器人视觉-语言-动作（VLA）领域面临的数据获取成本高、缺乏标准化基准以及模拟与现实世界差距大等挑战，本文提出了RealMirror，一个全面的开源具身AI VLA平台。RealMirror构建了一个高效、低成本的数据收集、模型训练和推理系统，无需真实机器人即可实现端到端VLA研究。为了促进模型演进和公平比较，还引入了一个专门针对人形机器人的VLA基准，包含多个场景、丰富的轨迹和各种VLA模型。此外，通过集成生成模型和3D高斯溅射来重建逼真的环境和机器人模型，成功演示了零样本Sim2Real迁移，即完全在模拟数据上训练的模型可以在真实机器人上无缝执行任务，无需任何微调。总之，RealMirror统一了这些关键组件，提供了一个强大的框架，显著加速了人形机器人VLA模型的开发。

## 🔬 方法详解

**问题定义**：现有的人形机器人VLA研究受限于数据获取的高昂成本，缺乏统一的评估基准，以及模拟环境与真实环境之间的巨大差异。这些问题阻碍了VLA模型的发展和实际应用。现有方法难以在真实机器人上直接应用，需要大量的真实数据进行微调，成本高昂。

**核心思路**：RealMirror的核心思路是构建一个全面的、开源的VLA平台，该平台能够以低成本的方式收集数据、训练模型和进行推理，同时提供一个标准化的基准用于模型评估和比较。通过结合生成模型和3D高斯溅射技术，实现模拟环境到真实环境的零样本迁移，从而降低对真实数据的依赖。

**技术框架**：RealMirror平台包含以下几个主要模块：1) 数据收集模块，用于高效、低成本地收集VLA数据；2) 模型训练模块，支持各种VLA模型的训练；3) 模型推理模块，用于在模拟和真实环境中进行模型推理；4) VLA基准，提供多个场景、丰富的轨迹和各种VLA模型，用于模型评估和比较；5) Sim2Real迁移模块，利用生成模型和3D高斯溅射技术，实现零样本Sim2Real迁移。

**关键创新**：RealMirror的关键创新在于其全面的平台设计和零样本Sim2Real迁移能力。通过提供一个完整的VLA研究框架，降低了研究门槛，加速了VLA模型的发展。零样本Sim2Real迁移技术减少了对真实数据的依赖，降低了模型部署成本。

**关键设计**：RealMirror平台的关键设计包括：1) 高效的数据收集策略，例如使用程序化生成和数据增强技术；2) 标准化的VLA基准，提供统一的评估指标和场景；3) 基于生成模型和3D高斯溅射的Sim2Real迁移方法，通过重建逼真的环境和机器人模型，减少模拟和真实环境之间的差异。

## 📊 实验亮点

RealMirror平台成功实现了零样本Sim2Real迁移，在模拟环境中训练的VLA模型可以直接在真实机器人上执行任务，无需任何微调。这一结果表明，该平台能够有效降低对真实数据的依赖，提高模型的泛化能力。此外，该平台提供的VLA基准为模型评估和比较提供了一个标准化的平台。

## 🎯 应用场景

RealMirror平台可广泛应用于人形机器人的控制、导航、物体操作等任务。该平台降低了VLA研究的门槛，加速了相关技术的发展，有望推动人形机器人在家庭服务、医疗护理、工业自动化等领域的应用。未来，该平台可以扩展到其他类型的机器人，并与其他AI技术相结合，实现更智能、更自主的机器人系统。

## 📄 摘要（原文）

> The emerging field of Vision-Language-Action (VLA) for humanoid robots faces several fundamental challenges, including the high cost of data acquisition, the lack of a standardized benchmark, and the significant gap between simulation and the real world. To overcome these obstacles, we propose RealMirror, a comprehensive, open-source embodied AI VLA platform. RealMirror builds an efficient, low-cost data collection, model training, and inference system that enables end-to-end VLA research without requiring a real robot. To facilitate model evolution and fair comparison, we also introduce a dedicated VLA benchmark for humanoid robots, featuring multiple scenarios, extensive trajectories, and various VLA models. Furthermore, by integrating generative models and 3D Gaussian Splatting to reconstruct realistic environments and robot models, we successfully demonstrate zero-shot Sim2Real transfer, where models trained exclusively on simulation data can perform tasks on a real robot seamlessly, without any fine-tuning. In conclusion, with the unification of these critical components, RealMirror provides a robust framework that significantly accelerates the development of VLA models for humanoid robots. Project page: https://terminators2025.github.io/RealMirror.github.io

