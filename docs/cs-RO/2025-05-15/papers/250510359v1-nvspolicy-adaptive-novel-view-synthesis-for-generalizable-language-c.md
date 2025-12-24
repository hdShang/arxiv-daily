---
layout: default
title: "NVSPolicy: Adaptive Novel-View Synthesis for Generalizable Language-Conditioned Policy Learning"
---

# NVSPolicy: Adaptive Novel-View Synthesis for Generalizable Language-Conditioned Policy Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.10359" class="toolbar-btn" target="_blank">📄 arXiv: 2505.10359v1</a>
  <a href="https://arxiv.org/pdf/2505.10359.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.10359v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.10359v1', 'NVSPolicy: Adaptive Novel-View Synthesis for Generalizable Language-Conditioned Policy Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Le Shi, Yifei Shi, Xin Xu, Tenglong Liu, Junhua Xi, Chengyuan Chen

**分类**: cs.RO, cs.CV

**发布日期**: 2025-05-15

---

## 💡 一句话要点

**提出NVSPolicy以解决机器人在复杂环境中的政策学习问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言条件政策学习` `深度生成模型` `新视图合成` `分层政策网络` `机器人操作`

## 📋 核心要点

1. 现有方法在生成图像时存在视觉伪影，导致机器人在复杂环境中的操作能力受限。
2. NVSPolicy通过自适应新视图合成模块和分层政策网络，动态生成信息丰富的视图图像以增强视觉上下文。
3. 在CALVIN数据集上，NVSPolicy实现了90.4%的平均成功率，显著优于其他方法，验证了其有效性。

## 📝 摘要（中文）

近年来，深度生成模型在零-shot泛化能力方面取得了显著进展，为机器人在非结构化环境中的操作提供了巨大潜力。通过对场景的部分观察，深度生成模型能够生成未见区域，从而提供更多上下文，增强机器人在未知环境中的泛化能力。然而，由于生成图像中的视觉伪影和多模态特征在政策学习中的低效整合，这一方向仍然面临挑战。本文提出了NVSPolicy，一种通用的语言条件政策学习方法，结合了自适应新视图合成模块和分层政策网络。NVSPolicy动态选择信息丰富的视角，并合成自适应的新视图图像，以丰富视觉上下文。为减轻合成图像的不完美影响，我们采用了循环一致的变分自编码器机制，将视觉特征解耦为语义特征和剩余特征，分别输入分层政策网络。大量实验表明，NVSPolicy在CALVIN上实现了90.4%的平均成功率，显著优于现有方法。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在复杂环境中政策学习的挑战，现有方法在生成图像时常出现视觉伪影，影响机器人操作的准确性和有效性。

**核心思路**：NVSPolicy通过结合自适应新视图合成模块与分层政策网络，动态生成信息丰富的视图图像，以增强机器人对环境的理解和决策能力。

**技术框架**：NVSPolicy的整体架构包括输入图像处理、自适应视图选择与合成、特征解耦、以及分层政策网络。输入图像经过处理后，系统动态选择最佳视角并合成新视图图像，随后将视觉特征解耦为语义特征和剩余特征，分别输入到分层政策网络中进行决策。

**关键创新**：最重要的创新在于自适应新视图合成模块与循环一致的变分自编码器机制的结合，能够有效减轻合成图像的伪影影响，并实现特征的有效解耦。

**关键设计**：在网络结构上，采用分层政策网络设计，语义特征用于高层次的元技能选择，剩余特征则用于低层次的动作估计。此外，损失函数设计上采用循环一致性损失，以确保生成图像的质量和一致性。

## 📊 实验亮点

在CALVIN数据集上的实验结果显示，NVSPolicy实现了90.4%的平均成功率，显著高于其他最新方法，验证了其在复杂环境中政策学习的有效性和优越性。通过消融研究，进一步确认了自适应新视图合成的关键作用。

## 🎯 应用场景

NVSPolicy的研究成果在机器人操作、自动化制造、智能家居等领域具有广泛的应用潜力。通过提高机器人在复杂和未知环境中的操作能力，该方法能够推动智能机器人在实际场景中的应用，提升其自主决策和操作的效率与准确性。

## 📄 摘要（原文）

> Recent advances in deep generative models demonstrate unprecedented zero-shot generalization capabilities, offering great potential for robot manipulation in unstructured environments. Given a partial observation of a scene, deep generative models could generate the unseen regions and therefore provide more context, which enhances the capability of robots to generalize across unseen environments. However, due to the visual artifacts in generated images and inefficient integration of multi-modal features in policy learning, this direction remains an open challenge. We introduce NVSPolicy, a generalizable language-conditioned policy learning method that couples an adaptive novel-view synthesis module with a hierarchical policy network. Given an input image, NVSPolicy dynamically selects an informative viewpoint and synthesizes an adaptive novel-view image to enrich the visual context. To mitigate the impact of the imperfect synthesized images, we adopt a cycle-consistent VAE mechanism that disentangles the visual features into the semantic feature and the remaining feature. The two features are then fed into the hierarchical policy network respectively: the semantic feature informs the high-level meta-skill selection, and the remaining feature guides low-level action estimation. Moreover, we propose several practical mechanisms to make the proposed method efficient. Extensive experiments on CALVIN demonstrate the state-of-the-art performance of our method. Specifically, it achieves an average success rate of 90.4\% across all tasks, greatly outperforming the recent methods. Ablation studies confirm the significance of our adaptive novel-view synthesis paradigm. In addition, we evaluate NVSPolicy on a real-world robotic platform to demonstrate its practical applicability.

