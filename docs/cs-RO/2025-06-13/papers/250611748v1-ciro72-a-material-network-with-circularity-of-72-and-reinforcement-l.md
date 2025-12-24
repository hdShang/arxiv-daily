---
layout: default
title: "CIRO7.2: A Material Network with Circularity of -7.2 and Reinforcement-Learning-Controlled Robotic Disassembler"
---

# CIRO7.2: A Material Network with Circularity of -7.2 and Reinforcement-Learning-Controlled Robotic Disassembler

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11748" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11748v1</a>
  <a href="https://arxiv.org/pdf/2506.11748.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11748v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11748v1', 'CIRO7.2: A Material Network with Circularity of -7.2 and Reinforcement-Learning-Controlled Robotic Disassembler')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Federico Zocco, Monica Malvezzi

**分类**: cs.RO, cs.CY

**发布日期**: 2025-06-13

**备注**: To be submitted

---

## 💡 一句话要点

**提出CIRO7.2以解决线性经济下的废物管理问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `循环经济` `废物管理` `强化学习` `机器人技术` `热力学` `材料网络` `资源回收` `循环智能`

## 📋 核心要点

1. 现有线性经济模式将使用后的产品视为废物，导致资源浪费和管理难题。
2. 论文提出了一种基于热力学的材料网络模型，结合强化学习控制的机器人拆解器，提升材料的循环利用率。
3. 实验结果显示，拆解不同数量的材料对循环性影响显著，最高循环性为-2.1，最低为-7.2，且与材料的关键性相关。

## 📝 摘要（中文）

随着对自然矿产资源的竞争加剧，线性经济模式导致大量废物的产生，管理问题亟待解决。本文通过增强循环经济的概念，提出了一种基于热力学的材料网络模型，结合强化学习控制的机器人拆解器，处理两种不同关键系数的固体材料。研究表明，拆解不同数量和重量的材料对循环性有显著影响，最高循环性为-2.1，最低为-7.2。此外，敏感性分析显示，强化学习控制器的性能与材料的数量和关键性呈正相关。该研究为循环智能与机器人领域奠定了基础，源代码已公开。

## 🔬 方法详解

**问题定义**：本文旨在解决线性经济模式下的废物管理问题，现有方法未能有效利用废弃物资源，导致资源浪费和环境问题。

**核心思路**：通过增强循环经济的概念，结合热力学原理，设计了一种材料网络模型，并利用强化学习控制机器人拆解器，以提高材料的循环利用率。

**技术框架**：整体架构包括材料网络模型、机器人拆解器和强化学习控制模块。材料网络处理两种固体材料，机器人拆解器负责实际拆解过程，强化学习算法优化拆解策略。

**关键创新**：最重要的创新在于将热力学与强化学习结合，提出了新的循环性指标λ，并通过实验验证了不同拆解策略对循环性的影响。

**关键设计**：在设计中，设置了不同的材料关键系数和拆解重量，使用了先进的强化学习算法，并进行了敏感性分析以评估控制器性能对循环性的影响。

## 📊 实验亮点

实验结果显示，在拆解2个1公斤材料时，循环性达到最高值-2.1，而在拆解4个1公斤材料时，循环性降至-7.2。敏感性分析表明，强化学习控制器的性能与材料数量和关键性呈正相关，显示出显著的优化潜力。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在废物管理、资源回收和机器人技术领域。通过提升材料的循环利用率，不仅能减少环境负担，还能推动向循环经济的转型，具有重要的社会和经济价值。

## 📄 摘要（原文）

> The competition over natural reserves of minerals is expected to increase in part because of the linear-economy paradigm based on take-make-dispose. Simultaneously, the linear economy considers end-of-use products as waste rather than as a resource, which results in large volumes of waste whose management remains an unsolved problem. Since a transition to a circular economy can mitigate these open issues, in this paper we begin by enhancing the notion of circularity based on compartmental dynamical thermodynamics, namely, $λ$, and then, we model a thermodynamical material network processing a batch of 2 solid materials of criticality coefficients of 0.1 and 0.95, with a robotic disassembler compartment controlled via reinforcement learning (RL), and processing 2-7 kg of materials. Subsequently, we focused on the design of the robotic disassembler compartment using state-of-the-art RL algorithms and assessing the algorithm performance with respect to $λ$ (Fig. 1). The highest circularity is -2.1 achieved in the case of disassembling 2 parts of 1 kg each, whereas it reduces to -7.2 in the case of disassembling 4 parts of 1 kg each contained inside a chassis of 3 kg. Finally, a sensitivity analysis highlighted that the impact on $λ$ of the performance of an RL controller has a positive correlation with the quantity and the criticality of the materials to be disassembled. This work also gives the principles of the emerging research fields indicated as circular intelligence and robotics (CIRO). Source code is publicly available.

