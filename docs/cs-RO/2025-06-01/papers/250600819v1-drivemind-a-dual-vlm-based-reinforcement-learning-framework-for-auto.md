---
layout: default
title: DriveMind: A Dual-VLM based Reinforcement Learning Framework for Autonomous Driving
---

# DriveMind: A Dual-VLM based Reinforcement Learning Framework for Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00819" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00819v1</a>
  <a href="https://arxiv.org/pdf/2506.00819.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00819v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00819v1', 'DriveMind: A Dual-VLM based Reinforcement Learning Framework for Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dawood Wasif, Terrence J Moore, Chandan K Reddy, Jin-Hee Cho

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-01

---

## 💡 一句话要点

**提出DriveMind框架以解决自主驾驶中的适应性与安全性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自主驾驶` `强化学习` `视觉-语言模型` `动态提示生成` `安全模块` `语义奖励` `跨域对齐`

## 📋 核心要点

1. 现有的自主驾驶方法缺乏透明性和适应性，无法有效应对动态驾驶环境中的变化。
2. DriveMind通过引入语义奖励框架，结合对比视觉-语言模型和动态提示生成，增强了系统的适应性和安全性。
3. 在CARLA Town 2的实验中，DriveMind的表现超越基线，展示了显著的成功率和安全性提升。

## 📝 摘要（中文）

端到端自主驾驶系统直接将传感器数据映射到控制指令，但仍然缺乏透明性、可解释性和正式的安全保障。尽管近期的视觉-语言引导强化学习方法引入了语义反馈，但通常依赖静态提示和固定目标，限制了对动态驾驶场景的适应性。本文提出DriveMind，一个统一的语义奖励框架，集成了对比视觉-语言模型编码器、基于新颖性触发的VLM编码器-解码器、分层安全模块和紧凑的预测世界模型。DriveMind在CARLA Town 2中实现了19.4 +/- 2.3 km/h的平均速度、0.98 +/- 0.03的路线完成率和近零碰撞，成功率比基线提高超过4%。其语义奖励在真实行车记录仪数据上实现零-shot泛化，展示了强大的跨域对齐能力和实际部署潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有自主驾驶系统在动态场景下的适应性不足和安全性缺乏的问题。现有方法通常依赖静态提示，无法有效应对环境变化。

**核心思路**：DriveMind框架通过引入语义奖励机制和动态提示生成，增强了系统的适应性和安全性，允许系统在复杂环境中进行实时调整。

**技术框架**：DriveMind的整体架构包括四个主要模块：对比视觉-语言模型编码器用于语义锚定；新颖性触发的VLM编码器-解码器用于动态提示生成；分层安全模块用于执行运动约束；紧凑的预测世界模型用于奖励与理想状态的对齐。

**关键创新**：最重要的创新在于结合了对比学习和动态提示生成，使得系统能够在语义漂移时实时调整策略，这与传统静态方法形成鲜明对比。

**关键设计**：在设计中，采用了链式思维蒸馏方法对VLM进行微调，确保动态提示的生成与环境变化相适应，同时分层安全模块确保了运动约束的执行。

## 📊 实验亮点

DriveMind在CARLA Town 2的实验中实现了19.4 +/- 2.3 km/h的平均速度和0.98 +/- 0.03的路线完成率，几乎没有碰撞，成功率比基线提高超过4%。其语义奖励机制在真实行车记录仪数据上实现了零-shot泛化，展示了强大的跨域对齐能力。

## 🎯 应用场景

DriveMind框架具有广泛的应用潜力，尤其是在城市自主驾驶、智能交通系统和无人驾驶车辆等领域。其增强的适应性和安全性使其在复杂和动态环境中表现出色，未来可望在实际驾驶场景中得到部署，提升道路安全性和驾驶效率。

## 📄 摘要（原文）

> End-to-end autonomous driving systems map sensor data directly to control commands, but remain opaque, lack interpretability, and offer no formal safety guarantees. While recent vision-language-guided reinforcement learning (RL) methods introduce semantic feedback, they often rely on static prompts and fixed objectives, limiting adaptability to dynamic driving scenes. We present DriveMind, a unified semantic reward framework that integrates: (i) a contrastive Vision-Language Model (VLM) encoder for stepwise semantic anchoring; (ii) a novelty-triggered VLM encoder-decoder, fine-tuned via chain-of-thought (CoT) distillation, for dynamic prompt generation upon semantic drift; (iii) a hierarchical safety module enforcing kinematic constraints (e.g., speed, lane centering, stability); and (iv) a compact predictive world model to reward alignment with anticipated ideal states. DriveMind achieves 19.4 +/- 2.3 km/h average speed, 0.98 +/- 0.03 route completion, and near-zero collisions in CARLA Town 2, outperforming baselines by over 4% in success rate. Its semantic reward generalizes zero-shot to real dash-cam data with minimal distributional shift, demonstrating robust cross-domain alignment and potential for real-world deployment.

