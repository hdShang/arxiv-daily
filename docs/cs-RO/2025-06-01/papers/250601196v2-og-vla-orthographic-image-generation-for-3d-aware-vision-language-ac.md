---
layout: default
title: "OG-VLA: Orthographic Image Generation for 3D-Aware Vision-Language Action Model"
---

# OG-VLA: Orthographic Image Generation for 3D-Aware Vision-Language Action Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.01196" class="toolbar-btn" target="_blank">📄 arXiv: 2506.01196v2</a>
  <a href="https://arxiv.org/pdf/2506.01196.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.01196v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.01196v2', 'OG-VLA: Orthographic Image Generation for 3D-Aware Vision-Language Action Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ishika Singh, Ankit Goyal, Stan Birchfield, Dieter Fox, Animesh Garg, Valts Blukis

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-06-01 (更新: 2025-11-18)

**备注**: 13 pages

---

## 💡 一句话要点

**提出OG-VLA以解决3D感知与语言指令映射问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `3D感知` `机器人操作` `自然语言处理` `点云渲染` `泛化能力` `智能系统`

## 📋 核心要点

1. 现有的3D感知机器人策略在面对未见指令和场景时泛化能力不足，限制了其应用范围。
2. OG-VLA通过将输入观察反投影为点云并从正交视图渲染，结合视觉和语言模型，提升了3D感知策略的泛化能力。
3. 在Arnold和Colosseum基准测试中，OG-VLA展示了超过40%的相对提升，同时在已见环境中保持了稳健的性能。

## 📝 摘要（中文）

我们介绍了OG-VLA，这是一种新颖的架构和学习框架，结合了视觉语言行动模型（VLA）的泛化能力与3D感知策略的鲁棒性。该方法解决了将自然语言指令与RGBD观察映射到准静态机器人动作的挑战。尽管3D感知机器人策略在精确的机器人操作任务上表现出色，但在面对未见指令、场景和物体时却难以泛化。相反，VLA在指令和场景的泛化上表现优异，但对相机和机器人姿态变化敏感。我们利用语言和视觉基础模型中嵌入的先验知识来提高3D感知关键帧策略的泛化能力。OG-VLA将来自不同视角的输入观察反投影为点云，然后从规范正交视图渲染，确保输入视图的不变性和输入输出空间的一致性。评估结果表明，在Arnold和Colosseum基准上，OG-VLA在未见环境中的泛化能力达到了最先进水平，相对提升超过40%。

## 🔬 方法详解

**问题定义**：本论文旨在解决将自然语言指令与RGBD观察映射到准静态机器人动作的挑战。现有的3D感知机器人策略在未见指令和场景的泛化能力上存在不足，而视觉语言行动模型在指令泛化上表现优异但对环境变化敏感。

**核心思路**：OG-VLA的核心思路是通过将输入观察反投影为点云并从规范正交视图渲染，利用语言和视觉模型的先验知识来提升3D感知策略的泛化能力。这种设计确保了输入视图的不变性和输入输出空间的一致性。

**技术框架**：OG-VLA的整体架构包括多个主要模块：首先，将RGBD观察反投影为点云；其次，从规范正交视图渲染这些点云；然后，使用视觉骨干网络、一个大型语言模型（LLM）和图像扩散模型生成编码末端执行器下一个位置和方向的图像。

**关键创新**：OG-VLA的最重要创新在于其将3D感知与语言模型有效结合，克服了现有方法在泛化能力和环境适应性上的不足。这种方法在输入视图不变性和输出一致性方面具有显著优势。

**关键设计**：在设计中，OG-VLA采用了特定的损失函数来优化生成图像的质量，并通过调整网络结构以适应不同的输入视角和环境变化，确保了模型的鲁棒性和泛化能力。

## 📊 实验亮点

OG-VLA在Arnold和Colosseum基准测试中展示了超过40%的相对提升，证明了其在未见环境中的优越泛化能力，同时在已见环境中保持了稳健的性能，显示出该方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操作、智能家居和自动化制造等。通过提高机器人对自然语言指令的理解和执行能力，OG-VLA可以在复杂环境中实现更高效的任务执行，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We introduce OG-VLA, a novel architecture and learning framework that combines the generalization strengths of Vision Language Action models (VLAs) with the robustness of 3D-aware policies. We address the challenge of mapping natural language instructions and one or more RGBD observations to quasi-static robot actions. 3D-aware robot policies achieve state-of-the-art performance on precise robot manipulation tasks, but struggle with generalization to unseen instructions, scenes, and objects. On the other hand, VLAs excel at generalizing across instructions and scenes, but can be sensitive to camera and robot pose variations. We leverage prior knowledge embedded in language and vision foundation models to improve generalization of 3D-aware keyframe policies. OG-VLA unprojects input observations from diverse views into a point cloud which is then rendered from canonical orthographic views, ensuring input view invariance and consistency between input and output spaces. These canonical views are processed with a vision backbone, a Large Language Model (LLM), and an image diffusion model to generate images that encode the next position and orientation of the end-effector on the input scene. Evaluations on the Arnold and Colosseum benchmarks demonstrate state-of-the-art generalization to unseen environments, with over 40% relative improvements while maintaining robust performance in seen settings. We also show real-world adaption in 3 to 5 demonstrations along with strong generalization. Videos and resources at https://og-vla.github.io/

