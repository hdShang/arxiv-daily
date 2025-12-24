---
layout: default
title: "Revisiting Power System Stabilizers with Increased Inverter-Based Generation: A Case Study"
---

# Revisiting Power System Stabilizers with Increased Inverter-Based Generation: A Case Study

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19357" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19357v2</a>
  <a href="https://arxiv.org/pdf/2506.19357.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19357v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19357v2', 'Revisiting Power System Stabilizers with Increased Inverter-Based Generation: A Case Study')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jovan Krajacic, Keith Moffat, Gustavo Valverde

**分类**: eess.SY

**发布日期**: 2025-06-24 (更新: 2025-11-06)

---

## 💡 一句话要点

**调整电力系统稳定器以应对逆变器发电的挑战**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `电力系统` `逆变器发电` `电力系统稳定器` `动态特性` `小信号稳定性` `调谐方法` `系统稳定性` `在线调谐`

## 📋 核心要点

1. 随着逆变器发电资源的增加，电力系统的动态特性发生了变化，导致系统稳定性面临挑战。
2. 本文提出通过调整电力系统稳定器（PSS）设置来恢复系统稳定性，特别关注模型基于的调谐方法。
3. 研究表明，现有调谐方法在协调有限的情况下效果不佳，推动了本地和自适应在线调谐方法的必要性。

## 📝 摘要（中文）

随着电力系统中逆变器发电资源（IBRs）比例的增加，其动态特性发生了显著变化，可能导致系统运行不稳定，出现阻尼不足的振荡或小信号转子角不稳定。本文研究了电力系统稳定器（PSS）设置调整是否能有效恢复系统稳定性，并在Kundur两区系统的基准案例中评估了基于模型的残差和P-Vref PSS调谐方法在不断变化的电网条件下的有效性。研究结果表明，这些调谐方法的有效性并不总是得到保证，特别是在协调有限的情况下。因此，本文的案例研究激励了本地和自适应在线PSS调谐方法的开发。

## 🔬 方法详解

**问题定义**：本文旨在解决在逆变器发电资源增加的背景下，电力系统稳定器（PSS）设置调整对系统稳定性的影响。现有方法在高IBR渗透率下的有效性存在不足，可能导致系统振荡和不稳定。

**核心思路**：论文的核心思路是评估不同的PSS调谐方法在动态变化的电网条件下的有效性，特别是模型基于的残差和P-Vref调谐方法，以确定其在提高系统稳定性方面的作用。

**技术框架**：研究采用Kundur两区系统作为基准案例，分析PSS设置的调整对系统动态响应的影响。主要模块包括模型建立、调谐方法评估和稳定性分析。

**关键创新**：本文的主要创新在于揭示了在高IBR渗透率下，传统PSS调谐方法的局限性，并提出了本地和自适应在线调谐方法的必要性，以应对系统动态特性的变化。

**关键设计**：研究中采用了基于模型的残差和P-Vref调谐方法，重点关注参数设置和调谐过程中的协调性，以确保在不同电网条件下的有效性。具体的参数设置和损失函数设计尚未详细披露。

## 📊 实验亮点

实验结果表明，基于模型的PSS调谐方法在高IBR渗透率下的有效性并不总是得到保证，特别是在协调有限的情况下。研究推动了本地和自适应在线调谐方法的开发，旨在提高系统的稳定性和响应能力。

## 🎯 应用场景

该研究的潜在应用领域包括电力系统的实时监控与控制，尤其是在高比例逆变器发电资源的电网中。通过优化电力系统稳定器的设置，可以提高电网的稳定性和可靠性，降低因振荡引发的故障风险，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> As power systems evolve with increasing production from Inverter-Based Resources (IBRs), their underlying dynamics are undergoing significant changes that can jeopardize system operation, leading to poorly damped oscillations or small-signal rotor angle instability. In this work, we investigate whether Power System Stabilizer (PSS) setting adjustments can effectively restore system stability and provide adequate damping in systems with increased IBR penetration, using the benchmark Kundur Two-Area System as a case study. Specifically, we evaluate the model-based Residues and P-Vref PSS tuning methods to examine their effectiveness under evolving grid conditions. Our findings indicate that the effectiveness of these tuning methods is not guaranteed, particularly when coordination is limited. Consequently, our case study motivates local and adaptive online PSS tuning methods.

