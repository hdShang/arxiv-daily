---
layout: default
title: "VFP: Variational Flow-Matching Policy for Multi-Modal Robot Manipulation"
---

# VFP: Variational Flow-Matching Policy for Multi-Modal Robot Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01622" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01622v2</a>
  <a href="https://arxiv.org/pdf/2508.01622.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01622v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01622v2', 'VFP: Variational Flow-Matching Policy for Multi-Modal Robot Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuanran Zhai, Qianyou Zhao, Qiaojun Yu, Ce Hao

**分类**: cs.RO, cs.LG

**发布日期**: 2025-08-03 (更新: 2025-10-02)

---

## 💡 一句话要点

**提出变分流匹配策略以解决多模态机器人操控问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `变分流匹配` `多模态操控` `机器人学习` `Kantorovich最优传输` `专家混合解码器` `动作生成` `任务成功率` `高效推理`

## 📋 核心要点

1. 现有流匹配方法在处理多模态任务时表现不佳，容易导致行为模糊或平均化，影响复杂操控的效果。
2. 本文提出变分流匹配策略（VFP），通过引入变分潜在先验和Kantorovich最优传输，增强模式感知和多模态捕捉能力。
3. VFP在41个模拟任务和3个真实机器人任务中表现优异，成功率较标准流基线提高49%，且推理速度快，模型紧凑。

## 📝 摘要（中文）

基于流匹配的策略最近成为学习型机器人操控的有前景的方法，相较于基于扩散的方法在动作采样上具有显著加速。然而，传统的流匹配方法在多模态处理上存在困难，常常在复杂操控任务中导致行为的平均化或模糊化。为此，本文提出变分流匹配策略（VFP），引入变分潜在先验以实现模式感知的动作生成，并有效捕捉任务级和轨迹级的多模态性。VFP进一步结合Kantorovich最优传输（K-OT）进行分布级对齐，并利用专家混合解码器（MoE）实现模式专业化和高效推理。我们在41个模拟任务和3个真实机器人任务上全面评估VFP，证明其在模拟和现实环境中的有效性和采样效率。结果显示，VFP在模拟中相较于标准流基线的任务成功率提高了49%。

## 🔬 方法详解

**问题定义**：本文旨在解决传统流匹配方法在多模态机器人操控任务中的不足，特别是行为模糊和平均化的问题。现有方法在复杂任务中难以有效捕捉多样化的动作模式。

**核心思路**：提出变分流匹配策略（VFP），通过引入变分潜在先验来实现模式感知的动作生成，结合Kantorovich最优传输进行分布级对齐，从而有效捕捉任务和轨迹级的多模态性。

**技术框架**：VFP的整体架构包括变分潜在先验、Kantorovich最优传输模块和专家混合解码器（MoE）。变分潜在先验用于生成多样化的动作，K-OT用于优化分布对齐，而MoE则实现模式专业化和高效推理。

**关键创新**：VFP的主要创新在于引入变分潜在先验和K-OT，使得模型能够在多模态任务中有效捕捉不同的动作模式，避免了传统方法的模糊化问题。

**关键设计**：在设计中，VFP采用了特定的损失函数以优化模式生成，并通过专家混合解码器实现高效的推理过程，确保模型在保持紧凑性的同时具备良好的性能。

## 📊 实验亮点

在实验中，VFP在41个模拟任务中相较于标准流基线的任务成功率提高了49%。在真实机器人任务中，VFP同样表现优异，展示了其在多模态操控中的有效性和高效推理能力。

## 🎯 应用场景

该研究的潜在应用领域包括工业机器人、服务机器人和医疗机器人等多模态操控场景。通过提高机器人在复杂任务中的操控能力，VFP能够显著提升机器人在实际应用中的灵活性和效率，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Flow-matching-based policies have recently emerged as a promising approach for learning-based robot manipulation, offering significant acceleration in action sampling compared to diffusion-based policies. However, conventional flow-matching methods struggle with multi-modality, often collapsing to averaged or ambiguous behaviors in complex manipulation tasks. To address this, we propose the Variational Flow-Matching Policy (VFP), which introduces a variational latent prior for mode-aware action generation and effectively captures both task-level and trajectory-level multi-modality. VFP further incorporates Kantorovich Optimal Transport (K-OT) for distribution-level alignment and utilizes a Mixture-of-Experts (MoE) decoder for mode specialization and efficient inference. We comprehensively evaluate VFP on 41 simulated tasks and 3 real-robot tasks, demonstrating its effectiveness and sampling efficiency in both simulated and real-world settings. Results show that VFP achieves a 49% relative improvement in task success rate over standard flow-based baselines in simulation, and further outperforms them on real-robot tasks, while still maintaining fast inference and a compact model size. More details are available on our project page: https://sites.google.com/view/varfp/

