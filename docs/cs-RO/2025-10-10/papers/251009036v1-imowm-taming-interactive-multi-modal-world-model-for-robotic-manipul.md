---
layout: default
title: iMoWM: Taming Interactive Multi-Modal World Model for Robotic Manipulation
---

# iMoWM: Taming Interactive Multi-Modal World Model for Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.09036" class="toolbar-btn" target="_blank">📄 arXiv: 2510.09036v1</a>
  <a href="https://arxiv.org/pdf/2510.09036.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.09036v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.09036v1', 'iMoWM: Taming Interactive Multi-Modal World Model for Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chuanrui Zhang, Zhengxian Wu, Guanxing Lu, Yansong Tang, Ziwei Wang

**分类**: cs.RO

**发布日期**: 2025-10-10

**🔗 代码/项目**: [PROJECT_PAGE](https://xingyoujun.github.io/imowm/)

---

## 💡 一句话要点

**提出iMoWM，利用交互式多模态世界模型提升机器人操作能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `世界模型` `机器人操作` `多模态学习` `深度学习` `强化学习`

## 📋 核心要点

1. 现有2D视频世界模型缺乏几何推理能力，难以有效模拟3D物理世界，限制了机器人操作的性能。
2. iMoWM通过自回归生成彩色图像、深度图和机械臂掩码，并使用MMTokenizer将多模态信息压缩为紧凑的token表示。
3. 实验表明，iMoWM提升了未来预测的视觉质量，并有效支持基于模型的强化学习和模仿学习。

## 📝 摘要（中文）

本文提出了一种名为iMoWM的交互式世界模型，旨在提升机器人操作能力。现有基于2D视频的世界模型缺乏几何和空间推理能力，难以捕捉3D世界的物理结构。iMoWM通过自回归方式生成彩色图像、深度图和机器人手臂掩码，并以动作为条件。为了克服三维信息带来的高计算成本，论文提出了MMTokenizer，将多模态输入统一为紧凑的token表示。这使得iMoWM能够利用大规模预训练的VideoGPT模型，同时保持高效率并融入更丰富的物理信息。凭借其多模态表示，iMoWM不仅提高了未来预测的视觉质量，还可作为基于模型的强化学习（MBRL）的有效模拟器，并促进真实世界的模仿学习。大量实验表明，iMoWM在这些任务中表现优异，展示了多模态世界建模在机器人操作中的优势。

## 🔬 方法详解

**问题定义**：现有基于视频的世界模型在机器人操作任务中面临挑战，主要原因是它们难以捕捉3D环境的几何和空间信息。这些模型通常只关注2D图像，忽略了深度信息和机器人自身状态，导致预测精度和泛化能力受限。因此，如何有效地将多模态信息融入世界模型，并降低计算复杂度，是亟待解决的问题。

**核心思路**：iMoWM的核心思路是构建一个能够理解和生成多模态信息的交互式世界模型。通过同时预测彩色图像、深度图和机器人手臂掩码，模型能够更全面地理解环境和自身状态。利用MMTokenizer将多模态信息压缩成token表示，从而降低计算成本，并允许模型利用预训练的VideoGPT模型。

**技术框架**：iMoWM的整体框架包括以下几个主要模块：1) 多模态编码器：将彩色图像、深度图和机器人手臂掩码编码成特征向量。2) MMTokenizer：将多模态特征向量转换为离散的token表示。3) VideoGPT：利用预训练的VideoGPT模型，根据历史token和动作预测未来的token。4) 多模态解码器：将预测的token解码成彩色图像、深度图和机器人手臂掩码。整个流程以自回归的方式进行，即每次预测都依赖于之前的预测结果和动作。

**关键创新**：iMoWM的关键创新在于MMTokenizer的设计，它能够有效地将多模态信息压缩成紧凑的token表示。与直接使用原始图像和深度图作为输入相比，MMTokenizer显著降低了计算复杂度，并允许模型利用大规模预训练的VideoGPT模型。此外，iMoWM的多模态输出也使得模型能够更全面地理解环境和自身状态。

**关键设计**：MMTokenizer使用可学习的码本将多模态特征向量量化为离散的token。具体来说，它将每个模态的特征向量映射到码本中最接近的码字，并将码字的索引作为token。损失函数包括重构损失和对抗损失，用于保证重构图像的质量和token表示的判别性。VideoGPT使用Transformer架构，并采用因果注意力机制，以保证自回归预测的正确性。

## 📊 实验亮点

实验结果表明，iMoWM在未来预测任务中取得了显著的性能提升，尤其是在深度图预测方面。与基线方法相比，iMoWM能够生成更清晰、更准确的深度图，从而提高了对3D环境的理解能力。此外，iMoWM在基于模型的强化学习任务中也表现出色，能够更快地学习到有效的操作策略。

## 🎯 应用场景

iMoWM具有广泛的应用前景，可用于机器人操作、自动驾驶、虚拟现实等领域。它可以作为机器人强化学习的模拟器，加速策略学习过程。此外，iMoWM还可以用于模仿学习，使机器人能够模仿人类的操作行为。通过不断与环境交互，iMoWM可以不断学习和改进，从而实现更智能、更灵活的机器人控制。

## 📄 摘要（原文）

> Learned world models hold significant potential for robotic manipulation, as they can serve as simulator for real-world interactions. While extensive progress has been made in 2D video-based world models, these approaches often lack geometric and spatial reasoning, which is essential for capturing the physical structure of the 3D world. To address this limitation, we introduce iMoWM, a novel interactive world model designed to generate color images, depth maps, and robot arm masks in an autoregressive manner conditioned on actions. To overcome the high computational cost associated with three-dimensional information, we propose MMTokenizer, which unifies multi-modal inputs into a compact token representation. This design enables iMoWM to leverage large-scale pretrained VideoGPT models while maintaining high efficiency and incorporating richer physical information. With its multi-modal representation, iMoWM not only improves the visual quality of future predictions but also serves as an effective simulator for model-based reinforcement learning (MBRL) and facilitates real-world imitation learning. Extensive experiments demonstrate the superiority of iMoWM across these tasks, showcasing the advantages of multi-modal world modeling for robotic manipulation. Homepage: https://xingyoujun.github.io/imowm/

