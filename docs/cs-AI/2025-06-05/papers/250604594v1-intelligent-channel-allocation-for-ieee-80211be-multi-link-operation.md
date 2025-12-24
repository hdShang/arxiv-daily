---
layout: default
title: "Intelligent Channel Allocation for IEEE 802.11be Multi-Link Operation: When MAB Meets LLM"
---

# Intelligent Channel Allocation for IEEE 802.11be Multi-Link Operation: When MAB Meets LLM

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04594" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04594v1</a>
  <a href="https://arxiv.org/pdf/2506.04594.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04594v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04594v1', 'Intelligent Channel Allocation for IEEE 802.11be Multi-Link Operation: When MAB Meets LLM')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shumin Lian, Jingwen Tong, Jun Zhang, Liqun Fu

**分类**: cs.NI, cs.AI, eess.SP

**发布日期**: 2025-06-05

**备注**: This work has been accepted by JSAC 2025

---

## 💡 一句话要点

**提出BAI-MCTS与LLM-BAI-MCTS以解决WiFi 7动态信道分配问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `动态信道分配` `多链路操作` `多臂老虎机` `蒙特卡洛树搜索` `大型语言模型` `WiFi 7` `网络优化`

## 📋 核心要点

1. 现有研究主要集中在静态WiFi 7网络配置下的性能分析，未能有效解决动态信道分配问题。
2. 本文提出将动态信道分配问题建模为组合优化问题，并利用多臂老虎机框架进行在线学习，设计了BAI-MCTS算法。
3. 实验结果显示，BAI-MCTS算法在达到98%最优值时，其收敛速度比现有最优算法快约50.44%。

## 📝 摘要（中文）

WiFi网络在全球范围内实现了无缝通信和数据交换。IEEE 802.11be标准（即WiFi 7）引入了多链路操作（MLO），允许设备在不同频段和信道上同时建立多个连接。尽管MLO在网络吞吐量和延迟方面具有显著优势，但在密集网络环境中信道分配仍面临重大挑战。本文将动态信道分配问题建模为组合优化问题，并在多臂老虎机（MAB）框架下进行在线学习，提出了基于最佳臂识别的蒙特卡洛树搜索（BAI-MCTS）算法，并结合大型语言模型（LLM）提出了LLM-BAI-MCTS算法。实验结果表明，BAI-MCTS算法的收敛速度比现有算法快约50.44%，而LLM-BAI-MCTS在密集网络中的收敛速度提升超过63.32%。

## 🔬 方法详解

**问题定义**：本文针对密集WiFi 7网络中的动态信道分配问题，现有方法在信道分配时缺乏有效的动态适应性，导致性能下降。

**核心思路**：通过将信道分配问题建模为组合优化问题，利用多臂老虎机（MAB）框架进行在线学习，以实现动态信道的最优分配。

**技术框架**：整体架构包括信道分配模型、基于MAB的在线学习机制和BAI-MCTS算法。BAI-MCTS通过识别最佳臂来优化信道选择，并结合LLM进一步提升性能。

**关键创新**：提出了BAI-MCTS算法及其与LLM的结合，显著提高了动态信道分配的效率和准确性，解决了现有方法在动态环境下的不足。

**关键设计**：在算法设计中，设置了样本复杂度和误差概率的上界，并通过数值实验验证了算法在不同网络场景下的适应性和有效性。

## 📊 实验亮点

BAI-MCTS算法在达到98%最优值时，其收敛速度比现有最优算法快约50.44%。而LLM-BAI-MCTS算法在密集网络中的收敛速度提升超过63.32%，显示出显著的性能优势。

## 🎯 应用场景

该研究的潜在应用领域包括智能家居、企业网络和公共WiFi等密集环境，能够有效提升网络性能和用户体验。未来，随着WiFi 7的普及，本文提出的动态信道分配算法将对网络管理和优化产生深远影响。

## 📄 摘要（原文）

> WiFi networks have achieved remarkable success in enabling seamless communication and data exchange worldwide. The IEEE 802.11be standard, known as WiFi 7, introduces Multi-Link Operation (MLO), a groundbreaking feature that enables devices to establish multiple simultaneous connections across different bands and channels. While MLO promises substantial improvements in network throughput and latency reduction, it presents significant challenges in channel allocation, particularly in dense network environments. Current research has predominantly focused on performance analysis and throughput optimization within static WiFi 7 network configurations. In contrast, this paper addresses the dynamic channel allocation problem in dense WiFi 7 networks with MLO capabilities. We formulate this challenge as a combinatorial optimization problem, leveraging a novel network performance analysis mechanism. Given the inherent lack of prior network information, we model the problem within a Multi-Armed Bandit (MAB) framework to enable online learning of optimal channel allocations. Our proposed Best-Arm Identification-enabled Monte Carlo Tree Search (BAI-MCTS) algorithm includes rigorous theoretical analysis, providing upper bounds for both sample complexity and error probability. To further reduce sample complexity and enhance generalizability across diverse network scenarios, we put forth LLM-BAI-MCTS, an intelligent algorithm for the dynamic channel allocation problem by integrating the Large Language Model (LLM) into the BAI-MCTS algorithm. Numerical results demonstrate that the BAI-MCTS algorithm achieves a convergence rate approximately $50.44\%$ faster than the state-of-the-art algorithms when reaching $98\%$ of the optimal value. Notably, the convergence rate of the LLM-BAI-MCTS algorithm increases by over $63.32\%$ in dense networks.

