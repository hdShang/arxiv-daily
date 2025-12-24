---
layout: default
title: LEAD: Minimizing Learner-Expert Asymmetry in End-to-End Driving
---

# LEAD: Minimizing Learner-Expert Asymmetry in End-to-End Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20563" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20563v1</a>
  <a href="https://arxiv.org/pdf/2512.20563.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20563v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20563v1', 'LEAD: Minimizing Learner-Expert Asymmetry in End-to-End Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Long Nguyen, Micha Fauth, Bernhard Jaeger, Daniel Dauner, Maximilian Igl, Andreas Geiger, Kashyap Chitta

**分类**: cs.CV, cs.AI, cs.LG, cs.RO

**发布日期**: 2025-12-23

**🔗 代码/项目**: [GITHUB](https://github.com/autonomousvision/lead)

---

## 💡 一句话要点

**LEAD：最小化端到端驾驶中学习者-专家不对称性，提升CARLA模拟器驾驶性能**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `端到端驾驶` `模仿学习` `信息不对称` `CARLA模拟器` `感知监督`

## 📋 核心要点

1. 现有模仿学习方法在模拟驾驶中面临专家与学习者信息不对称的挑战，专家拥有更全面的环境信息和更明确的导航意图。
2. LEAD旨在通过缩小专家和学习者之间的差距来提高模仿学习的性能，包括提升学习者的感知能力和明确导航意图。
3. TransFuser v6在CARLA基准测试中取得了显著的性能提升，并在NAVSIM和Waymo数据集上验证了其sim-to-real的有效性。

## 📝 摘要（中文）

模拟器可以生成几乎无限的驾驶数据，但模拟环境中的模仿学习策略仍然难以实现鲁棒的闭环性能。本文研究了专家演示和基于传感器的学生观测之间的不对称性如何限制模仿学习的有效性。专家具有更高的可见性（例如，忽略遮挡）和更低的不确定性（例如，知道其他车辆的动作），这使得学生难以可靠地模仿。此外，学生模型在测试时仅通过单个目标点来指定导航意图（即要遵循的路线），这导致导航意图不明确。研究表明，这些不对称性会显著限制CARLA中的驾驶性能，并提出了解决这些问题的有效干预措施。经过仔细修改以缩小专家和学生之间的差距后，TransFuser v6 (TFv6) 学生策略在所有主要的公开CARLA闭环基准测试中都达到了新的state-of-the-art，在Bench2Drive上达到95 DS，并在Longest6 v2和Town13上实现了超过两倍的性能提升。此外，通过将来自数据集的感知监督集成到共享的sim-to-real流水线中，在NAVSIM和Waymo Vision-Based End-to-End驾驶基准测试中也显示出一致的收益。代码、数据和模型已公开。

## 🔬 方法详解

**问题定义**：现有端到端驾驶模仿学习方法在模拟环境中表现不佳，主要原因是专家（提供训练数据）和学习者（实际驾驶策略）之间存在信息不对称。专家通常拥有更全面的环境信息（例如，无遮挡的全局视图，其他车辆的未来动作），而学习者只能依赖有限的传感器数据。此外，学习者在测试时仅通过单个目标点来指定导航意图，这与专家在训练时所拥有的完整路线信息不符。这些不对称性导致学习者难以有效地模仿专家的驾驶行为。

**核心思路**：LEAD的核心思路是最小化专家和学习者之间的信息不对称性。具体来说，通过增强学习者的感知能力，使其能够更好地理解周围环境；同时，通过更明确地指定导航意图，帮助学习者更好地规划行驶路线。这样，学习者就能更有效地模仿专家的驾驶行为，从而提高整体驾驶性能。

**技术框架**：LEAD方法基于TransFuser架构，并对其进行了改进。整体框架包括以下几个主要模块：1) 感知模块：用于从传感器数据中提取环境信息；2) 导航模块：用于根据目标点和环境信息规划行驶路线；3) 控制模块：用于根据行驶路线生成车辆控制指令。此外，LEAD还引入了感知监督，利用数据集中的标注信息来提高感知模块的准确性。

**关键创新**：LEAD最重要的技术创新点在于其对专家-学习者不对称性的显式建模和解决。与以往的研究主要关注模型架构的改进不同，LEAD更加关注数据层面的问题，通过缩小专家和学习者之间的差距来提高模仿学习的性能。这种思路为解决端到端驾驶中的挑战提供了一个新的视角。

**关键设计**：LEAD的关键设计包括：1) 使用更强大的感知模块，例如，TransFuser v6；2) 引入感知监督，利用数据集中的标注信息来提高感知模块的准确性；3) 采用更有效的导航策略，例如，通过预测未来轨迹来明确导航意图；4) 仔细调整训练策略，例如，使用数据增强来模拟不同的环境条件。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20563v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20563v1/gfx/teaser-short.png" alt="img_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

TransFuser v6在CARLA闭环基准测试中取得了显著的性能提升，在Bench2Drive上达到了95 DS，并在Longest6 v2和Town13上实现了超过两倍的性能提升。此外，通过将感知监督集成到sim-to-real流水线中，在NAVSIM和Waymo Vision-Based End-to-End驾驶基准测试中也显示出一致的收益。这些结果表明，LEAD方法能够有效地提高端到端驾驶模仿学习的性能。

## 🎯 应用场景

LEAD的研究成果可以应用于自动驾驶系统的开发，特别是在模拟环境中的训练和验证。通过缩小模拟环境和真实环境之间的差距，可以更有效地训练自动驾驶策略，并提高其在真实世界中的鲁棒性和安全性。此外，该方法还可以应用于其他需要模仿学习的机器人任务，例如，无人机导航和操作。

## 📄 摘要（原文）

> Simulators can generate virtually unlimited driving data, yet imitation learning policies in simulation still struggle to achieve robust closed-loop performance. Motivated by this gap, we empirically study how misalignment between privileged expert demonstrations and sensor-based student observations can limit the effectiveness of imitation learning. More precisely, experts have significantly higher visibility (e.g., ignoring occlusions) and far lower uncertainty (e.g., knowing other vehicles' actions), making them difficult to imitate reliably. Furthermore, navigational intent (i.e., the route to follow) is under-specified in student models at test time via only a single target point. We demonstrate that these asymmetries can measurably limit driving performance in CARLA and offer practical interventions to address them. After careful modifications to narrow the gaps between expert and student, our TransFuser v6 (TFv6) student policy achieves a new state of the art on all major publicly available CARLA closed-loop benchmarks, reaching 95 DS on Bench2Drive and more than doubling prior performances on Longest6~v2 and Town13. Additionally, by integrating perception supervision from our dataset into a shared sim-to-real pipeline, we show consistent gains on the NAVSIM and Waymo Vision-Based End-to-End driving benchmarks. Our code, data, and models are publicly available at https://github.com/autonomousvision/lead.

