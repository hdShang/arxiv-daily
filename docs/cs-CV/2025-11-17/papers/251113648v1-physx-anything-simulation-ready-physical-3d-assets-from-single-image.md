---
layout: default
title: "PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image"
---

# PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.13648" class="toolbar-btn" target="_blank">📄 arXiv: 2511.13648v1</a>
  <a href="https://arxiv.org/pdf/2511.13648.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.13648v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.13648v1', 'PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziang Cao, Fangzhou Hong, Zhaoxi Chen, Liang Pan, Ziwei Liu

**分类**: cs.CV, cs.RO

**发布日期**: 2025-11-17

**备注**: Project page: https://physx-anything.github.io/

---

## 💡 一句话要点

**PhysX-Anything：首个单图生成可用于仿真的物理3D资产框架**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `物理3D生成` `具身智能` `视觉语言模型` `几何token化` `仿真机器人`

## 📋 核心要点

1. 现有3D生成方法忽略了物理和关节属性，限制了其在具身智能中的应用。
2. PhysX-Anything提出基于VLM的物理3D生成模型和高效的几何token化方法，生成高质量的sim-ready 3D资产。
3. PhysX-Mobility数据集扩展了对象类别，实验证明PhysX-Anything具有强大的生成性能和泛化能力。

## 📝 摘要（中文）

本文提出PhysX-Anything，首个simulation-ready的物理3D生成框架，仅需单张图片即可生成高质量、可用于仿真的3D资产，包含显式几何结构、关节信息和物理属性。该框架包含首个基于VLM的物理3D生成模型，以及一种高效的几何结构token化表示方法，将token数量减少193倍，从而在标准VLM token预算内实现显式几何学习，且无需在微调期间引入任何特殊token，显著提升生成质量。此外，为了克服现有物理3D数据集多样性不足的问题，构建了新的数据集PhysX-Mobility，将对象类别扩展了2倍以上，包含超过2000个具有丰富物理标注的常见真实世界对象。在PhysX-Mobility和真实图像上的大量实验表明，PhysX-Anything具有强大的生成性能和鲁棒的泛化能力。在MuJoCo风格环境中的仿真实验验证了生成的sim-ready资产可以直接用于contact-rich的机器人策略学习。PhysX-Anything有望推动具身智能和基于物理的仿真等下游应用。

## 🔬 方法详解

**问题定义**：现有3D建模方法主要关注静态视觉表示，缺乏对物理属性和关节信息的建模，导致生成的3D模型无法直接用于仿真和交互，限制了其在具身智能等领域的应用。现有物理3D数据集的多样性不足，也限制了模型的泛化能力。

**核心思路**：PhysX-Anything的核心思路是利用视觉语言模型（VLM）的强大生成能力，结合一种高效的几何结构token化表示方法，从单张图像中生成包含显式几何结构、关节信息和物理属性的3D资产。通过减少几何结构的token数量，可以在标准VLM的token预算内进行显式几何学习，从而提高生成质量。

**技术框架**：PhysX-Anything框架主要包含以下几个模块：1) 基于VLM的物理3D生成模型，用于从单张图像中生成3D资产的几何结构、关节信息和物理属性；2) 高效的几何结构token化表示方法，用于将3D几何结构转换为VLM可以处理的token序列；3) PhysX-Mobility数据集，用于训练和评估模型。整体流程是从单张图像输入到VLM，生成token序列，然后解码为3D资产。

**关键创新**：PhysX-Anything的关键创新点在于：1) 提出了首个基于VLM的物理3D生成模型，可以直接从单张图像生成sim-ready的3D资产；2) 提出了一种高效的几何结构token化表示方法，显著减少了token数量，从而可以在标准VLM的token预算内进行显式几何学习。与现有方法的本质区别在于，PhysX-Anything能够生成包含物理属性和关节信息的3D资产，可以直接用于仿真和交互。

**关键设计**：几何结构token化表示方法是关键设计之一，通过体素化和八叉树编码等技术，将3D几何结构转换为紧凑的token序列，显著减少了token数量。损失函数的设计也至关重要，需要平衡几何结构、关节信息和物理属性的生成质量。具体的网络结构和参数设置未知。

## 📊 实验亮点

PhysX-Anything在PhysX-Mobility数据集上取得了显著的生成性能提升。通过高效的几何结构token化方法，token数量减少了193倍，使得在标准VLM token预算下进行显式几何学习成为可能。仿真实验表明，生成的3D资产可以直接用于MuJoCo环境中的机器人策略学习，验证了其sim-ready的特性。

## 🎯 应用场景

PhysX-Anything生成的sim-ready 3D资产可以直接用于机器人策略学习、虚拟现实、游戏开发等领域。例如，可以利用生成的3D模型训练机器人在复杂环境中的操作技能，或者构建逼真的虚拟环境用于用户交互。该研究有望推动具身智能和基于物理的仿真技术的发展。

## 📄 摘要（原文）

> 3D modeling is shifting from static visual representations toward physical, articulated assets that can be directly used in simulation and interaction. However, most existing 3D generation methods overlook key physical and articulation properties, thereby limiting their utility in embodied AI. To bridge this gap, we introduce PhysX-Anything, the first simulation-ready physical 3D generative framework that, given a single in-the-wild image, produces high-quality sim-ready 3D assets with explicit geometry, articulation, and physical attributes. Specifically, we propose the first VLM-based physical 3D generative model, along with a new 3D representation that efficiently tokenizes geometry. It reduces the number of tokens by 193x, enabling explicit geometry learning within standard VLM token budgets without introducing any special tokens during fine-tuning and significantly improving generative quality. In addition, to overcome the limited diversity of existing physical 3D datasets, we construct a new dataset, PhysX-Mobility, which expands the object categories in prior physical 3D datasets by over 2x and includes more than 2K common real-world objects with rich physical annotations. Extensive experiments on PhysX-Mobility and in-the-wild images demonstrate that PhysX-Anything delivers strong generative performance and robust generalization. Furthermore, simulation-based experiments in a MuJoCo-style environment validate that our sim-ready assets can be directly used for contact-rich robotic policy learning. We believe PhysX-Anything can substantially empower a broad range of downstream applications, especially in embodied AI and physics-based simulation.

