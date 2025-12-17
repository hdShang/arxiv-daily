---
layout: default
title: MV-Performer: Taming Video Diffusion Model for Faithful and Synchronized Multi-view Performer Synthesis
---

# MV-Performer: Taming Video Diffusion Model for Faithful and Synchronized Multi-view Performer Synthesis

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.07190" target="_blank" class="toolbar-btn">arXiv: 2510.07190v1</a>
    <a href="https://arxiv.org/pdf/2510.07190.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07190v1" 
            onclick="toggleFavorite(this, '2510.07190v1', 'MV-Performer: Taming Video Diffusion Model for Faithful and Synchronized Multi-view Performer Synthesis')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yihao Zhi, Chenghong Li, Hongjie Liao, Xihe Yang, Zhengwentai Sun, Jiahao Chang, Xiaodong Cun, Wensen Feng, Xiaoguang Han

**分类**: cs.CV

**发布日期**: 2025-10-08

**备注**: Accepted by SIGGRAPH Asia 2025 conference track

---

## 💡 一句话要点

**MV-Performer：提出一种用于生成逼真同步多视角表演者视频的扩散模型**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `多视角视频生成` `扩散模型` `新视角合成` `人体建模` `视频同步`

## 📋 核心要点

1. 现有视频生成方法难以生成360度视角变化，尤其是在以人为中心的场景中，存在视角切换时的同步性问题。
2. MV-Performer利用多视角数据集MVHumanNet，并引入相机相关的法线贴图作为条件信号，缓解视角模糊性。
3. 通过多视角扩散模型融合参考视频、部分渲染和不同视点信息，并设计鲁棒的推理过程，提升生成视频的质量和同步性。

## 📝 摘要（中文）

本文提出MV-Performer，一个用于从单目全身捕捉生成同步新视角视频的创新框架，专注于以人为中心的子领域。为了实现360度合成，充分利用MVHumanNet数据集并结合信息丰富的条件信号。具体来说，使用从定向部分点云渲染的相机相关法线贴图，有效缓解可见和不可见观测之间的模糊性。为了保持生成视频的同步性，提出了一个以人为中心的多视角视频扩散模型，融合了来自参考视频、部分渲染和不同视点的信息。此外，还提供了一个鲁棒的推理过程，用于处理真实场景中的视频，大大减轻了由不完美的单目深度估计引起的伪影。在三个数据集上的大量实验证明了MV-Performer的先进性和鲁棒性，为以人为中心的4D新视角合成建立了一个强大的模型。

## 🔬 方法详解

**问题定义**：现有视频生成方法主要集中在正面视角的相机轨迹控制，难以生成360度视角变化，尤其是在以人为中心的场景中，单目深度估计的不准确性会导致伪影，且不同视角视频的同步性难以保证。

**核心思路**：利用扩散模型强大的生成能力，结合多视角数据集的优势，通过引入相机相关的法线贴图作为条件信号，来缓解视角模糊性，并设计多视角扩散模型来保证生成视频的同步性。

**技术框架**：MV-Performer框架包含以下几个主要模块：1) 使用单目深度估计方法从输入视频中提取深度信息；2) 从深度信息渲染相机相关的法线贴图；3) 将参考视频、法线贴图和目标视角信息输入到多视角扩散模型中；4) 扩散模型生成目标视角的视频。

**关键创新**：1) 提出使用相机相关的法线贴图作为条件信号，有效缓解了可见和不可见观测之间的模糊性，提升了360度视角合成的质量；2) 设计了多视角扩散模型，通过融合来自参考视频、部分渲染和不同视点的信息，保证了生成视频的同步性；3) 提出了一个鲁棒的推理过程，用于处理真实场景中的视频，减轻了由不完美的单目深度估计引起的伪影。

**关键设计**：多视角扩散模型采用U-Net结构，输入包括参考视频帧、法线贴图和目标视角信息。损失函数包括L1损失和感知损失，用于提升生成视频的质量。推理过程中，采用迭代细化的方式，逐步生成目标视角的视频。

## 📊 实验亮点

实验结果表明，MV-Performer在三个数据集上都取得了state-of-the-art的效果。与现有方法相比，MV-Performer生成的视频在视角一致性、人物逼真度和视频同步性方面都有显著提升。消融实验验证了相机相关法线贴图和多视角扩散模型设计的有效性。

## 🎯 应用场景

MV-Performer在虚拟现实、增强现实、游戏开发和电影制作等领域具有广泛的应用前景。它可以用于生成逼真的360度人物表演视频，为用户提供沉浸式的体验。此外，该技术还可以用于创建虚拟化身、进行动作捕捉和进行视频编辑等。

## 📄 摘要（原文）

> Recent breakthroughs in video generation, powered by large-scale datasets and diffusion techniques, have shown that video diffusion models can function as implicit 4D novel view synthesizers. Nevertheless, current methods primarily concentrate on redirecting camera trajectory within the front view while struggling to generate 360-degree viewpoint changes. In this paper, we focus on human-centric subdomain and present MV-Performer, an innovative framework for creating synchronized novel view videos from monocular full-body captures. To achieve a 360-degree synthesis, we extensively leverage the MVHumanNet dataset and incorporate an informative condition signal. Specifically, we use the camera-dependent normal maps rendered from oriented partial point clouds, which effectively alleviate the ambiguity between seen and unseen observations. To maintain synchronization in the generated videos, we propose a multi-view human-centric video diffusion model that fuses information from the reference video, partial rendering, and different viewpoints. Additionally, we provide a robust inference procedure for in-the-wild video cases, which greatly mitigates the artifacts induced by imperfect monocular depth estimation. Extensive experiments on three datasets demonstrate our MV-Performer's state-of-the-art effectiveness and robustness, setting a strong model for human-centric 4D novel view synthesis.

