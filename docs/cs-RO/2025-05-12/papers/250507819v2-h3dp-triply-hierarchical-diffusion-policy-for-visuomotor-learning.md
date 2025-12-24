---
layout: default
title: H$^3$DP: Triply-Hierarchical Diffusion Policy for Visuomotor Learning
---

# H$^3$DP: Triply-Hierarchical Diffusion Policy for Visuomotor Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07819" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07819v2</a>
  <a href="https://arxiv.org/pdf/2505.07819.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07819v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07819v2', 'H$^3$DP: Triply-Hierarchical Diffusion Policy for Visuomotor Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiyang Lu, Yufeng Tian, Zhecheng Yuan, Xianbang Wang, Pu Hua, Zhengrong Xue, Huazhe Xu

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-05-12 (更新: 2025-06-17)

**🔗 代码/项目**: [PROJECT_PAGE](https://lyy-iiis.github.io/h3dp/)

---

## 💡 一句话要点

**提出H$^{	extbf{3}}$DP以解决视觉感知与动作预测耦合问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉运动学习` `机器人操作` `层次化策略` `深度学习` `多尺度表示` `扩散模型` `动作生成` `语义特征`

## 📋 核心要点

1. 现有的视觉运动策略学习方法多依赖生成模型，未能有效处理视觉感知与动作预测之间的耦合关系。
2. H$^{	extbf{3}}$DP通过三层次结构设计，增强视觉特征与动作生成的整合，提升了策略学习的效果。
3. 实验结果显示，H$^{	extbf{3}}$DP在44个仿真任务中平均提升27.5%，并在4个复杂的双手操作任务中表现优异。

## 📝 摘要（中文）

视觉运动策略学习在机器人操作中取得了显著进展，然而现有方法往往忽视了视觉感知与动作预测之间的关键耦合关系。本文提出了三层次层次化扩散策略（H$^{	extbf{3}}$DP），通过引入层次结构来增强视觉特征与动作生成之间的整合。H$^{	extbf{3}}$DP包含三个层次：基于深度信息的输入层次化、编码不同粒度语义特征的多尺度视觉表示，以及与相应视觉特征对齐的层次条件扩散过程。大量实验表明，H$^{	extbf{3}}$DP在44个仿真任务中相较于基线方法平均提升27.5%，并在4个具有挑战性的双手真实世界操作任务中表现优越。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉运动策略学习中视觉感知与动作预测之间的耦合不足问题。现有方法主要依赖生成模型，未能充分考虑视觉信息对动作生成的影响。

**核心思路**：H$^{	extbf{3}}$DP通过引入三层次的层次结构，强化视觉特征与动作生成的整合，具体包括深度感知、语义特征编码和层次条件扩散过程。

**技术框架**：H$^{	extbf{3}}$DP的整体架构包括三个主要模块：1) 深度感知输入层次化，组织RGB-D观察数据；2) 多尺度视觉表示，编码不同粒度的语义特征；3) 层次条件扩散过程，确保粗到细的动作生成与视觉特征的对齐。

**关键创新**：H$^{	extbf{3}}$DP的创新在于其三层次结构设计，显著改善了视觉信息与动作生成之间的耦合，区别于传统方法的单一生成模型。

**关键设计**：在设计中，H$^{	extbf{3}}$DP采用了深度信息进行输入层次化，使用多尺度卷积网络进行特征提取，并引入层次条件的损失函数来优化动作生成过程。

## 📊 实验亮点

H$^{	extbf{3}}$DP在44个仿真任务中实现了平均27.5%的性能提升，相较于基线方法表现出色。此外，在4个复杂的双手真实世界操作任务中，H$^{	extbf{3}}$DP也展现了优越的操作能力，证明了其有效性。

## 🎯 应用场景

H$^{	extbf{3}}$DP的研究成果在机器人操作、自动化制造和人机交互等领域具有广泛的应用潜力。通过更好地整合视觉信息与动作生成，该方法能够提升机器人在复杂环境中的操作能力，推动智能机器人技术的发展。

## 📄 摘要（原文）

> Visuomotor policy learning has witnessed substantial progress in robotic manipulation, with recent approaches predominantly relying on generative models to model the action distribution. However, these methods often overlook the critical coupling between visual perception and action prediction. In this work, we introduce $\textbf{Triply-Hierarchical Diffusion Policy}~(\textbf{H$^{\mathbf{3}}$DP})$, a novel visuomotor learning framework that explicitly incorporates hierarchical structures to strengthen the integration between visual features and action generation. H$^{3}$DP contains $\mathbf{3}$ levels of hierarchy: (1) depth-aware input layering that organizes RGB-D observations based on depth information; (2) multi-scale visual representations that encode semantic features at varying levels of granularity; and (3) a hierarchically conditioned diffusion process that aligns the generation of coarse-to-fine actions with corresponding visual features. Extensive experiments demonstrate that H$^{3}$DP yields a $\mathbf{+27.5\%}$ average relative improvement over baselines across $\mathbf{44}$ simulation tasks and achieves superior performance in $\mathbf{4}$ challenging bimanual real-world manipulation tasks. Project Page: https://lyy-iiis.github.io/h3dp/.

