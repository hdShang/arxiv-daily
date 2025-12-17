---
layout: default
title: Motion Planning for Safe Landing of a Human-Piloted Parafoil
---

# Motion Planning for Safe Landing of a Human-Piloted Parafoil

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.10595" class="toolbar-btn" target="_blank">📄 arXiv: 2512.10595v1</a>
  <a href="https://arxiv.org/pdf/2512.10595.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.10595v1" onclick="toggleFavorite(this, '2512.10595v1', 'Motion Planning for Safe Landing of a Human-Piloted Parafoil')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maximillian Fainkich, Kiril Solovey, Anna Clarke

**分类**: cs.RO

**发布日期**: 2025-12-11

---

## 💡 一句话要点

**提出基于改进SST算法的伞翼飞行运动规划方法，提升人控伞翼安全着陆性能。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `伞翼飞行` `运动规划` `安全着陆` `人机协作` `SST算法`

## 📋 核心要点

1. 现有伞翼飞行员训练依赖经验，缺乏有效模拟器，导致训练周期长且安全性难以保障。
2. 论文提出改进的Stable Sparse RRT (SST)算法，优化伞翼飞行轨迹，降低倾斜角，提升安全性。
3. 实验表明，该算法生成的轨迹在成本上优于人类飞行员20%-80%，验证了其在安全性和效率方面的潜力。

## 📝 摘要（中文）

大多数跳伞事故发生在伞翼飞行和着陆阶段，通常是由于飞行员在操控伞翼时判断失误造成的。由于缺乏功能完善且易于使用的训练模拟器，新手飞行员的培训周期较长。此外，适用于辅助人类训练的伞翼轨迹规划研究仍然有限。为了弥补这一差距，本文研究了人控伞翼飞行的安全轨迹计算问题，并考察了这些轨迹与人类生成的解决方案相比如何。在算法方面，我们改进了Li等人提出的基于采样的运动规划器Stable Sparse RRT (SST)，以应对问题约束，同时最小化倾斜角（控制工作量）作为安全性的代理。然后，我们将计算机生成的解决方案与来自人类生成的伞翼飞行数据进行比较，结果表明该算法的相对成本比人类飞行员的性能提高了20%-80%。我们观察到，人类飞行员倾向于首先缩小与着陆区域的水平距离，然后通过盘旋下降到适合开始着陆操作的高度来解决垂直差距。本文考虑的算法可以实现更平滑、更渐进的下降，并在保持安全约束的同时，以最终进近所需的精确高度到达着陆区域。总的来说，该研究证明了计算机生成的指导方针（而不是传统的经验法则）的潜力，这些指导方针可以集成到未来的模拟器中，以训练飞行员进行更安全、更具成本效益的飞行。

## 🔬 方法详解

**问题定义**：论文旨在解决人控伞翼飞行过程中，由于飞行员经验不足或判断失误导致的安全着陆问题。现有方法依赖人工经验，缺乏有效的轨迹规划工具，难以保证飞行安全和效率。

**核心思路**：论文的核心思路是利用运动规划算法，生成安全且高效的伞翼飞行轨迹，辅助飞行员进行训练和飞行。通过优化轨迹，降低飞行员的控制负担，减少操作失误的可能性，从而提高飞行安全性。

**技术框架**：该方法基于Stable Sparse RRT (SST)算法，并针对伞翼飞行的特点进行了改进。整体流程包括：1) 定义伞翼飞行的状态空间和控制空间；2) 构建伞翼飞行的动力学模型；3) 利用改进的SST算法生成候选轨迹；4) 评估轨迹的安全性、成本和可行性；5) 选择最优轨迹作为飞行指导。

**关键创新**：论文的关键创新在于将运动规划算法应用于人控伞翼飞行领域，并针对伞翼飞行的特殊约束条件，对SST算法进行了改进。通过最小化倾斜角作为安全性的代理，有效地降低了飞行员的控制负担，提高了飞行安全性。

**关键设计**：论文的关键设计包括：1) 针对伞翼飞行的动力学模型，考虑了空气阻力、升力等因素；2) 定义了倾斜角作为安全性的代理，并将其纳入优化目标；3) 改进了SST算法的采样策略，使其更适应伞翼飞行的状态空间。

## 📊 实验亮点

实验结果表明，与人类飞行员生成的轨迹相比，该算法生成的轨迹在成本上提高了20%-80%。这表明该算法能够有效地优化伞翼飞行轨迹，降低飞行员的控制负担，提高飞行安全性。

## 🎯 应用场景

该研究成果可应用于伞翼飞行员训练模拟器，为新手飞行员提供安全、高效的飞行指导。此外，该方法还可用于开发智能伞翼飞行系统，辅助飞行员进行飞行决策，提高飞行安全性，并可扩展到其他类似的人机协作飞行场景。

## 📄 摘要（原文）

> Most skydiving accidents occur during the parafoil-piloting and landing stages and result from human lapses in judgment while piloting the parafoil. Training of novice pilots is protracted due to the lack of functional and easily accessible training simulators. Moreover, work on parafoil trajectory planning suitable for aiding human training remains limited. To bridge this gap, we study the problem of computing safe trajectories for human-piloted parafoil flight and examine how such trajectories fare against human-generated solutions. For the algorithmic part, we adapt the sampling-based motion planner Stable Sparse RRT (SST) by Li et al., to cope with the problem constraints while minimizing the bank angle (control effort) as a proxy for safety. We then compare the computer-generated solutions with data from human-generated parafoil flight, where the algorithm offers a relative cost improvement of 20\%-80\% over the performance of the human pilot. We observe that human pilots tend to, first, close the horizontal distance to the landing area, and then address the vertical gap by spiraling down to the suitable altitude for starting a landing maneuver. The algorithm considered here makes smoother and more gradual descents, arriving at the landing area at the precise altitude necessary for the final approach while maintaining safety constraints. Overall, the study demonstrates the potential of computer-generated guidelines, rather than traditional rules of thumb, which can be integrated into future simulators to train pilots for safer and more cost-effective flights.

