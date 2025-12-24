---
layout: default
title: Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation
---

# Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20188" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20188v1</a>
  <a href="https://arxiv.org/pdf/2512.20188.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20188v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20188v1', 'Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Teqiang Zou, Hongliang Zeng, Yuxuan Nong, Yifan Li, Kehui Liu, Haotian Yang, Xinyang Ling, Xin Li, Lianyang Ma

**分类**: cs.RO, cs.AI

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**提出DuoCore-FS异步快速-慢速视觉-语言-动作策略，用于全身机器人操作。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言动作` `机器人操作` `异步执行` `快速-慢速策略` `全身控制`

## 📋 核心要点

1. 现有VLA系统受限于VLM的低推理速度，同步执行限制了全身机器人操作的实时性和控制稳定性。
2. DuoCore-FS框架通过异步执行VLM推理和动作生成，利用潜在表示缓冲区桥接快慢通道，提升整体性能。
3. 实验表明，DuoCore-FS能以30Hz生成全身动作块，速度是现有方法的3倍，并提高了真实环境下的任务成功率。

## 📝 摘要（中文）

大多数视觉-语言-动作（VLA）系统集成了视觉-语言模型（VLM）进行语义推理，以及动作专家生成连续动作信号，但两者通常以单一的统一频率运行。因此，策略性能受到大型VLM低推理速度的限制。这种强制同步执行严重限制了全身机器人操作中的控制稳定性和实时性能，全身机器人操作涉及更多关节、更大的运动空间和动态变化的视角。我们引入了一个真正的异步快速-慢速VLA框架（DuoCore-FS），将系统组织成一个用于高频动作生成的快速通道和一个用于丰富VLM推理的慢速通道。该系统的特点是两个关键特征。首先，一个潜在表示缓冲区桥接了慢速和快速系统。它存储与场景-指令上下文对齐的指令语义和动作推理表示，为快速通道提供高级指导。其次，一个全身动作分词器提供了全身动作的紧凑、统一的表示。重要的是，VLM和动作专家仍然进行端到端联合训练，在保持统一策略学习的同时实现异步执行。DuoCore-FS支持一个30亿参数的VLM，同时实现30 Hz的全身动作块生成，大约是先前具有可比模型大小的VLA模型的三倍。真实的全身操作实验表明，与同步快速-慢速VLA基线相比，任务成功率得到提高，响应能力显著增强。DuoCore-FS的实现，包括训练、推理和部署，由Astribot作为Astribot机器人平台的一部分提供给商业用户。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作（VLA）系统通常采用同步执行模式，即视觉-语言模型（VLM）的推理和动作专家的动作生成以相同的频率运行。然而，大型VLM的推理速度较慢，这限制了整个系统的实时性，尤其是在需要高频率控制的全身机器人操作中。此外，同步执行也限制了控制的稳定性，难以应对动态变化的环境。

**核心思路**：DuoCore-FS的核心思路是将VLA系统解耦为两个异步运行的通道：一个快速通道用于高频率的动作生成，一个慢速通道用于VLM的语义推理。通过这种方式，系统可以充分利用VLM的强大推理能力，同时避免其低速推理对实时性的影响。关键在于设计一个有效的机制，将慢速通道的推理结果传递给快速通道，指导其动作生成。

**技术框架**：DuoCore-FS框架包含以下主要模块：1) 慢速通道：负责运行VLM，进行视觉和语言信息的理解，提取场景和指令的语义信息。2) 快速通道：负责基于慢速通道提供的语义信息，生成高频率的动作指令。3) 潜在表示缓冲区：作为慢速通道和快速通道之间的桥梁，存储VLM推理得到的语义表示，并将其与场景-指令上下文对齐，为快速通道提供高级指导。4) 全身动作分词器：将全身动作表示为紧凑、统一的离散token序列，便于动作的生成和控制。

**关键创新**：DuoCore-FS最重要的创新点在于其异步执行的架构。与传统的同步VLA系统相比，DuoCore-FS允许VLM和动作专家以不同的频率运行，从而突破了VLM推理速度的瓶颈。此外，潜在表示缓冲区的引入，使得慢速通道的推理结果能够有效地指导快速通道的动作生成，保证了整体策略的一致性。

**关键设计**：DuoCore-FS的关键设计包括：1) 潜在表示缓冲区的实现方式，需要考虑如何有效地存储和检索语义表示，并将其与场景-指令上下文对齐。2) 全身动作分词器的设计，需要考虑如何将高维度的全身动作空间映射到低维度的token空间，同时保证动作的表达能力和控制精度。3) 损失函数的设计，需要保证VLM和动作专家能够进行端到端的联合训练，从而学习到统一的策略。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20188v1/framework.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20188v1/co_training.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20188v1/popcorn_pipeline.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

DuoCore-FS在真实环境下的全身操作实验中表现出色，实现了30Hz的全身动作块生成速度，是现有VLA模型的三倍。与同步Fast-Slow VLA基线相比，DuoCore-FS显著提高了任务成功率和响应能力。例如，在特定操作任务中，DuoCore-FS的任务成功率提升了XX%（具体数据未知）。

## 🎯 应用场景

DuoCore-FS框架在全身机器人操作领域具有广泛的应用前景，例如家庭服务机器人、工业自动化机器人等。该框架可以提高机器人的响应速度和控制精度，使其能够更好地完成复杂的任务，例如物体抓取、装配、导航等。此外，该框架还可以应用于虚拟现实、游戏等领域，提高虚拟角色的智能性和交互性。

## 📄 摘要（原文）

> Most Vision-Language-Action (VLA) systems integrate a Vision-Language Model (VLM) for semantic reasoning with an action expert generating continuous action signals, yet both typically run at a single unified frequency. As a result, policy performance is constrained by the low inference speed of large VLMs. This mandatory synchronous execution severely limits control stability and real-time performance in whole-body robotic manipulation, which involves more joints, larger motion spaces, and dynamically changing views. We introduce a truly asynchronous Fast-Slow VLA framework (DuoCore-FS), organizing the system into a fast pathway for high-frequency action generation and a slow pathway for rich VLM reasoning. The system is characterized by two key features. First, a latent representation buffer bridges the slow and fast systems. It stores instruction semantics and action-reasoning representation aligned with the scene-instruction context, providing high-level guidance to the fast pathway. Second, a whole-body action tokenizer provides a compact, unified representation of whole-body actions. Importantly, the VLM and action expert are still jointly trained end-to-end, preserving unified policy learning while enabling asynchronous execution. DuoCore-FS supports a 3B-parameter VLM while achieving 30 Hz whole-body action-chunk generation, approximately three times as fast as prior VLA models with comparable model sizes. Real-world whole-body manipulation experiments demonstrate improved task success rates and significantly enhanced responsiveness compared to synchronous Fast-Slow VLA baselines. The implementation of DuoCore-FS, including training, inference, and deployment, is provided to commercial users by Astribot as part of the Astribot robotic platform.

