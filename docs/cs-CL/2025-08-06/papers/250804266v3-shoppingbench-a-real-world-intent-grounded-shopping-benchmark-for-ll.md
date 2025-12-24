---
layout: default
title: "ShoppingBench: A Real-World Intent-Grounded Shopping Benchmark for LLM-based Agents"
---

# ShoppingBench: A Real-World Intent-Grounded Shopping Benchmark for LLM-based Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04266" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04266v3</a>
  <a href="https://arxiv.org/pdf/2508.04266.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04266v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04266v3', 'ShoppingBench: A Real-World Intent-Grounded Shopping Benchmark for LLM-based Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiangyuan Wang, Kejun Xiao, Qi Sun, Huaipeng Zhao, Tao Luo, Jian Dong Zhang, Xiaoyi Zeng

**分类**: cs.CL

**发布日期**: 2025-08-06 (更新: 2025-12-10)

**备注**: submit to AAAI2026

---

## 💡 一句话要点

**提出ShoppingBench以解决复杂购物意图评估问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `购物意图` `基准测试` `语言模型` `轨迹蒸馏` `电子商务` `用户体验` `强化学习`

## 📋 核心要点

1. 现有的电子商务基准主要集中在基本用户意图，无法有效评估复杂的购物场景和用户需求。
2. 提出ShoppingBench，一个新颖的购物基准，旨在模拟多样化的用户意图并提供真实的购物环境。
3. 实验结果显示，当前最先进的语言代理在ShoppingBench上的成功率低于50%，显示出其面临的挑战性。

## 📝 摘要（中文）

现有的电子商务基准主要关注基本用户意图，如寻找或购买产品。然而，现实用户往往追求更复杂的目标，如使用优惠券、管理预算和寻找多产品卖家。为此，我们提出了ShoppingBench，这是一个新颖的端到端购物基准，旨在涵盖越来越具有挑战性的意图。我们提出了一个可扩展的框架，基于真实世界产品的样本模拟用户指令。为了实现一致和可靠的评估，我们提供了一个大型购物沙箱，作为一个互动模拟环境，包含超过250万种真实产品。实验结果表明，即使是最先进的语言代理（如GPT-4.1）在我们的基准任务上的绝对成功率也低于50%，突显了ShoppingBench带来的重大挑战。此外，我们提出了一种轨迹蒸馏策略，并利用监督微调和强化学习在合成轨迹上，将大型语言代理的能力蒸馏到一个较小的代理中。最终，我们训练的代理在性能上与GPT-4.1相当。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有电子商务基准无法有效评估复杂用户意图的问题。现有方法主要关注基本的购物行为，未能涵盖用户在真实场景中的多样化需求和目标。

**核心思路**：我们提出ShoppingBench，通过模拟多种真实购物意图，构建一个端到端的购物基准，旨在提供更具挑战性的评估环境。该方法通过真实产品样本生成用户指令，增强了基准的实用性和有效性。

**技术框架**：整体架构包括一个大型购物沙箱，包含超过250万种真实产品，用户可以在此环境中进行互动。框架支持多种用户意图的模拟，并通过轨迹蒸馏策略提升代理的性能。

**关键创新**：本研究的主要创新在于提出了ShoppingBench这一新型基准，能够有效评估复杂的购物意图，并引入轨迹蒸馏策略，将大型语言模型的能力转移至较小模型，提升了模型的实用性。

**关键设计**：在设计中，我们采用了监督微调和强化学习相结合的方法，利用合成轨迹进行训练，确保代理在多样化意图下的表现能够与大型模型相媲美。

## 📊 实验亮点

实验结果表明，当前最先进的语言代理（如GPT-4.1）在ShoppingBench上的绝对成功率低于50%，显示出该基准的挑战性。同时，通过轨迹蒸馏策略，我们训练的代理在性能上与GPT-4.1相当，展现了显著的提升潜力。

## 🎯 应用场景

ShoppingBench的研究成果可广泛应用于电子商务平台、智能购物助手和个性化推荐系统等领域。通过更准确地理解和响应用户复杂的购物意图，该基准能够提升用户体验，并推动智能代理的进一步发展与应用。

## 📄 摘要（原文）

> Existing benchmarks in e-commerce primarily focus on basic user intents, such as finding or purchasing products. However, real-world users often pursue more complex goals, such as applying vouchers, managing budgets, and finding multi-products seller. To bridge this gap, we propose ShoppingBench, a novel end-to-end shopping benchmark designed to encompass increasingly challenging levels of grounded intent. Specifically, we propose a scalable framework to simulate user instructions based on various intents derived from sampled real-world products. To facilitate consistent and reliable evaluations, we provide a large-scale shopping sandbox that serves as an interactive simulated environment, incorporating over 2.5 million real-world products. Experimental results demonstrate that even state-of-the-art language agents (such as GPT-4.1) achieve absolute success rates under 50% on our benchmark tasks, highlighting the significant challenges posed by our ShoppingBench. In addition, we propose a trajectory distillation strategy and leverage supervised fine-tuning, along with reinforcement learning on synthetic trajectories, to distill the capabilities of a large language agent into a smaller one. As a result, our trained agent achieves competitive performance compared to GPT-4.1.

