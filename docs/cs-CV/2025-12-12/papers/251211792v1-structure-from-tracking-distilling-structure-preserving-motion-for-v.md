---
layout: default
title: Structure From Tracking: Distilling Structure-Preserving Motion for Video Generation
---

# Structure From Tracking: Distilling Structure-Preserving Motion for Video Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.11792" class="toolbar-btn" target="_blank">📄 arXiv: 2512.11792v1</a>
  <a href="https://arxiv.org/pdf/2512.11792.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.11792v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.11792v1', 'Structure From Tracking: Distilling Structure-Preserving Motion for Video Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yang Fei, George Stoica, Jingyuan Liu, Qifeng Chen, Ranjay Krishna, Xiaojuan Wang, Benlin Liu

**分类**: cs.CV

**发布日期**: 2025-12-12

**备注**: Project Website: https://sam2videox.github.io/

---

## 💡 一句话要点

**提出SAM2VideoX，通过蒸馏结构保持运动先验，提升视频生成质量。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视频生成` `扩散模型` `运动先验` `结构保持` `自回归模型`

## 📋 核心要点

1. 现有视频生成模型难以生成保持结构一致性的运动，尤其是在处理铰接和可变形物体时，单纯增加数据量无法解决。
2. 论文提出将自回归视频跟踪模型SAM2中的结构保持运动先验知识，提炼到双向视频扩散模型CogVideoX中，从而指导视频生成。
3. 实验表明，SAM2VideoX在VBench和人类评估中均优于现有基线方法，在结构保持和视频质量上取得了显著提升。

## 📝 摘要（中文）

现实世界是刚性约束和可变形结构的结合。对于视频模型而言，这意味着生成既能保持逼真度又能保持结构的运动。尽管扩散模型取得了进展，但生成逼真的、保持结构的运动仍然具有挑战性，特别是对于铰接式和可变形对象，如人类和动物。仅仅扩大训练数据规模未能解决物理上不合理的过渡。现有方法依赖于使用噪声运动表示（如光流或使用外部不完善模型提取的骨骼）进行条件约束。为了解决这些挑战，我们引入了一种算法，将结构保持运动先验从自回归视频跟踪模型(SAM2)提炼到双向视频扩散模型(CogVideoX)中。通过我们的方法，我们训练了SAM2VideoX，它包含两个创新：(1)一个双向特征融合模块，从像SAM2这样的循环模型中提取全局结构保持运动先验；(2)一个局部Gram流损失，用于对齐局部特征的移动方式。在VBench和人工研究上的实验表明，SAM2VideoX相比之前的基线方法，实现了持续的提升（在VBench上+2.60%，FVD降低21-22%，人类偏好度为71.4%）。具体来说，在VBench上，我们达到了95.51%，超过了REPA(92.91%) 2.60%，并将FVD降低到360.57，分别比REPA和LoRA微调提高了21.20%和22.46%。项目网站位于https://sam2videox.github.io/。

## 🔬 方法详解

**问题定义**：现有视频生成模型，特别是基于扩散模型的，在生成包含复杂运动（如人类或动物的运动）的视频时，难以保持生成视频中物体的结构一致性。简单地增加训练数据并不能有效解决这个问题，而且现有方法依赖于不完美的外部模型提取的运动信息（如光流或骨骼），这会引入噪声并限制生成质量。

**核心思路**：论文的核心思路是从一个已经具备较好跟踪能力的自回归模型（SAM2）中提取结构保持的运动先验，并将其迁移到扩散模型（CogVideoX）中。通过这种方式，扩散模型可以学习到更真实的运动模式，从而生成结构更稳定的视频。

**技术框架**：SAM2VideoX的整体框架包含两个主要部分：1) 使用双向特征融合模块从SAM2中提取全局结构保持运动先验；2) 使用局部Gram流损失来对齐局部特征的运动方式。SAM2首先作为运动信息的来源，其输出通过双向特征融合模块，为CogVideoX提供全局运动指导。CogVideoX则是一个标准的扩散模型，负责生成最终的视频帧。局部Gram流损失用于确保生成视频中局部特征的运动与SAM2的预测一致。

**关键创新**：论文的关键创新在于将自回归跟踪模型与扩散模型相结合，利用跟踪模型提供的结构保持运动先验来指导扩散模型的生成过程。双向特征融合模块和局部Gram流损失是实现这一目标的关键技术手段。与现有方法相比，该方法避免了直接使用噪声运动信息作为条件，而是通过蒸馏的方式学习运动先验，从而提高了生成视频的质量和结构一致性。

**关键设计**：双向特征融合模块的具体实现细节未知，但其核心思想是利用双向循环神经网络来捕捉SAM2在时间上的依赖关系，从而提取全局运动信息。局部Gram流损失通过计算生成视频和SAM2预测的局部特征之间的Gram矩阵，并最小化它们之间的差异，来保证局部运动的一致性。具体的损失函数形式和网络结构细节需要在论文原文中查找。

## 📊 实验亮点

SAM2VideoX在VBench基准测试中达到了95.51%的得分，超过了REPA的92.91%，提升了2.60%。同时，FVD指标降低到360.57，相比REPA和LoRA微调分别提升了21.20%和22.46%。人类评估结果显示，71.4%的人更偏好SAM2VideoX生成的视频，表明该方法在主观视觉质量上也有显著提升。

## 🎯 应用场景

该研究成果可应用于各种视频生成任务，例如：逼真的人物动画生成、动物运动模拟、以及各种需要保持结构一致性的视频内容创作。其潜在价值在于提升视频生成的真实感和可控性，为电影制作、游戏开发、虚拟现实等领域带来新的可能性。未来，该技术有望进一步扩展到更复杂的场景和更精细的运动控制。

## 📄 摘要（原文）

> Reality is a dance between rigid constraints and deformable structures. For video models, that means generating motion that preserves fidelity as well as structure. Despite progress in diffusion models, producing realistic structure-preserving motion remains challenging, especially for articulated and deformable objects such as humans and animals. Scaling training data alone, so far, has failed to resolve physically implausible transitions. Existing approaches rely on conditioning with noisy motion representations, such as optical flow or skeletons extracted using an external imperfect model. To address these challenges, we introduce an algorithm to distill structure-preserving motion priors from an autoregressive video tracking model (SAM2) into a bidirectional video diffusion model (CogVideoX). With our method, we train SAM2VideoX, which contains two innovations: (1) a bidirectional feature fusion module that extracts global structure-preserving motion priors from a recurrent model like SAM2; (2) a Local Gram Flow loss that aligns how local features move together. Experiments on VBench and in human studies show that SAM2VideoX delivers consistent gains (+2.60\% on VBench, 21-22\% lower FVD, and 71.4\% human preference) over prior baselines. Specifically, on VBench, we achieve 95.51\%, surpassing REPA (92.91\%) by 2.60\%, and reduce FVD to 360.57, a 21.20\% and 22.46\% improvement over REPA- and LoRA-finetuning, respectively. The project website can be found at https://sam2videox.github.io/ .

