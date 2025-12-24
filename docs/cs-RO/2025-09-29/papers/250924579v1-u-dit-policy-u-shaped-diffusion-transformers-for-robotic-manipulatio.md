---
layout: default
title: "U-DiT Policy: U-shaped Diffusion Transformers for Robotic Manipulation"
---

# U-DiT Policy: U-shaped Diffusion Transformers for Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24579" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24579v1</a>
  <a href="https://arxiv.org/pdf/2509.24579.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24579v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24579v1', 'U-DiT Policy: U-shaped Diffusion Transformers for Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Linzhi Wu, Aoran Mei, Xiyue Wang, Guo-Niu Zhu, Zhongxue Gan

**分类**: cs.RO

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**提出U-DiT Policy，结合U-Net和Transformer优势，提升机器人操作任务中Diffusion Policy的性能。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人操作` `扩散模型` `Transformer` `U-Net` `视觉运动控制`

## 📋 核心要点

1. 现有基于U-Net的扩散策略在机器人操作中存在全局上下文建模不足和过度平滑的问题。
2. U-DiT Policy结合U-Net的多尺度特征融合和Transformer的全局上下文建模能力，提升表征和策略表达能力。
3. 实验表明，U-DiT在仿真和真实机器人任务中均优于现有方法，尤其在泛化性和鲁棒性方面。

## 📝 摘要（中文）

本文提出了一种名为U-DiT Policy的新型U型扩散Transformer框架，用于解决机器人端到端视觉运动控制中，现有基于U-Net架构的扩散策略（DP-U）存在的全局上下文建模能力有限和过度平滑问题。U-DiT保留了U-Net的多尺度特征融合优势，同时集成了Transformer的全局上下文建模能力，从而增强了表征能力和策略表达能力。在仿真和真实机器人操作任务中进行了广泛的评估。在仿真中，U-DiT的平均性能比基线方法提高了10％，并且在可比参数预算下，超过了使用AdaLN块的基于Transformer的扩散策略（DP-T）6％。在真实机器人任务中，U-DiT表现出卓越的泛化性和鲁棒性，平均比DP-U提高了22.5％。此外，在干扰和光照变化下的鲁棒性和泛化实验进一步突出了U-DiT的优势。这些结果突出了U-DiT Policy作为基于扩散的机器人操作新基础的有效性和实际潜力。

## 🔬 方法详解

**问题定义**：现有基于U-Net架构的Diffusion Policy (DP-U)在机器人操作任务中，虽然有效，但存在两个主要痛点：一是全局上下文建模能力有限，难以捕捉长程依赖关系；二是容易产生过度平滑的伪影，影响生成动作的精度。

**核心思路**：U-DiT Policy的核心思路是将U-Net的多尺度特征融合能力与Transformer的全局上下文建模能力相结合。通过U-Net结构提取不同尺度的特征，再利用Transformer对这些特征进行全局建模，从而提升策略的表达能力和泛化性能。

**技术框架**：U-DiT Policy采用U型架构，类似于U-Net，但其核心构建块是Transformer。编码器部分逐步降低特征图的分辨率，并使用Transformer层提取特征；解码器部分则逐步恢复特征图的分辨率，同样使用Transformer层进行特征融合。跳跃连接（skip connection）将编码器和解码器中对应尺度的特征图连接起来，以保留细节信息。

**关键创新**：U-DiT的关键创新在于将Transformer引入到U-Net架构中，用于扩散模型的策略学习。与传统的DP-U相比，U-DiT能够更好地捕捉全局上下文信息，从而生成更准确、更鲁棒的动作序列。与纯Transformer结构的扩散策略（DP-T）相比，U-DiT保留了U-Net的多尺度特征融合优势，能够更好地处理图像输入。

**关键设计**：U-DiT使用Transformer作为其核心构建块，具体实现细节未知。论文中提到与DP-T相比，U-DiT在可比参数预算下性能更优，表明其在模型设计上可能进行了优化，例如高效的注意力机制或参数共享策略。损失函数方面，论文未明确说明，推测可能采用标准的扩散模型训练方法，例如最小化预测噪声与真实噪声之间的差异。

## 📊 实验亮点

U-DiT在仿真实验中，相比基线方法平均性能提升10%，相比基于Transformer的扩散策略（DP-T）提升6%（在可比参数量下）。在真实机器人操作任务中，U-DiT相比DP-U平均性能提升22.5%。在干扰和光照变化下，U-DiT展现出更强的鲁棒性和泛化能力。

## 🎯 应用场景

U-DiT Policy在机器人操作领域具有广泛的应用前景，例如物体抓取、装配、导航等。该方法可以应用于工业自动化、家庭服务机器人、医疗机器人等领域，提高机器人的智能化水平和工作效率。未来，U-DiT Policy有望成为机器人操作领域中一种重要的基础模型。

## 📄 摘要（原文）

> Diffusion-based methods have been acknowledged as a powerful paradigm for end-to-end visuomotor control in robotics. Most existing approaches adopt a Diffusion Policy in U-Net architecture (DP-U), which, while effective, suffers from limited global context modeling and over-smoothing artifacts. To address these issues, we propose U-DiT Policy, a novel U-shaped Diffusion Transformer framework. U-DiT preserves the multi-scale feature fusion advantages of U-Net while integrating the global context modeling capability of Transformers, thereby enhancing representational power and policy expressiveness. We evaluate U-DiT extensively across both simulation and real-world robotic manipulation tasks. In simulation, U-DiT achieves an average performance gain of 10\% over baseline methods and surpasses Transformer-based diffusion policies (DP-T) that use AdaLN blocks by 6\% under comparable parameter budgets. On real-world robotic tasks, U-DiT demonstrates superior generalization and robustness, achieving an average improvement of 22.5\% over DP-U. In addition, robustness and generalization experiments under distractor and lighting variations further highlight the advantages of U-DiT. These results highlight the effectiveness and practical potential of U-DiT Policy as a new foundation for diffusion-based robotic manipulation.

