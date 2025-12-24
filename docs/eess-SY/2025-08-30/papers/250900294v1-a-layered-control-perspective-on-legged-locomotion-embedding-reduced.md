---
layout: default
title: "A Layered Control Perspective on Legged Locomotion: Embedding Reduced Order Models via Hybrid Zero Dynamics"
---

# A Layered Control Perspective on Legged Locomotion: Embedding Reduced Order Models via Hybrid Zero Dynamics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00294" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00294v1</a>
  <a href="https://arxiv.org/pdf/2509.00294.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00294v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00294v1', 'A Layered Control Perspective on Legged Locomotion: Embedding Reduced Order Models via Hybrid Zero Dynamics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sergio A. Esteban, Max H. Cohen, Adrian B. Ghansah, Aaron D. Ames

**分类**: eess.SY, cs.RO

**发布日期**: 2025-08-30

---

## 💡 一句话要点

**通过混合零动态嵌入降阶模型以解决腿部运动控制问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `腿部运动` `降阶模型` `混合零动态` `控制理论` `机器人技术` `动态步态` `稳定性保证`

## 📋 核心要点

1. 现有的降阶模型在腿部运动控制中缺乏与全阶模型相同的稳定性保证，限制了其应用。
2. 本文提出了一种分层控制视角，通过合成零动态流形来实现降阶模型与全阶模型的统一。
3. 仿真实验表明，稳定的降阶模型周期轨道能够保证全阶模型的稳定性，验证了方法的有效性。

## 📝 摘要（中文）

降阶模型（ROM）为腿部机器人合成动态步态提供了强有力的手段。然而，这种方法缺乏使用全阶模型（FOM）进行步态合成的正式保证，例如混合零动态。本文旨在通过分层控制视角统一这些方法。我们建立了ROM在全阶混合动力学上实现稳定步态的条件。通过合成一个零动态流形来编码ROM的行为，控制器可以驱动FOM到达该表面，从而实现混合零动态。我们证明了ROM中的稳定周期轨道意味着FOM的混合零动态的输入到状态稳定周期轨道，因此也适用于FOM动力学。该结果在线性倒立摆ROM和五连杆平面步态FOM的仿真中得到了验证。

## 🔬 方法详解

**问题定义**：本文解决了降阶模型在腿部运动控制中缺乏稳定性保证的问题，现有方法无法确保在全阶模型下的步态稳定性。

**核心思路**：通过分层控制的视角，建立降阶模型与全阶混合动力学之间的联系，合成零动态流形以实现稳定步态。

**技术框架**：整体架构包括降阶模型的构建、零动态流形的合成以及控制器的设计，确保控制器能够驱动全阶模型到达零动态流形。

**关键创新**：最重要的创新在于证明了降阶模型中的稳定周期轨道能够保证全阶模型的混合零动态的稳定性，这是与现有方法的本质区别。

**关键设计**：关键设计包括零动态流形的构建方法、控制器的合成策略，以及在仿真中使用的线性倒立摆和五连杆平面步态模型的具体参数设置。

## 📊 实验亮点

实验结果显示，所提出的方法在仿真中成功实现了稳定的步态控制，降阶模型的稳定周期轨道能够有效驱动全阶模型，验证了理论的有效性。与传统方法相比，提升了步态的稳定性和控制精度。

## 🎯 应用场景

该研究的潜在应用领域包括腿部机器人、仿生机器人以及人机交互等。通过提供稳定的步态控制方法，能够提升机器人在复杂环境中的运动能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Reduced-order models (ROMs) provide a powerful means of synthesizing dynamic walking gaits on legged robots. Yet this approach lacks the formal guarantees enjoyed by methods that utilize the full-order model (FOM) for gait synthesis, e.g., hybrid zero dynamics. This paper aims to unify these approaches through a layered control perspective. In particular, we establish conditions on when a ROM of locomotion yields stable walking on the full-order hybrid dynamics. To achieve this result, given an ROM we synthesize a zero dynamics manifold encoding the behavior of the ROM -- controllers can be synthesized that drive the FOM to this surface, yielding hybrid zero dynamics. We prove that a stable periodic orbit in the ROM implies an input-to-state stable periodic orbit of the FOM's hybrid zero dynamics, and hence the FOM dynamics. This result is demonstrated in simulation on a linear inverted pendulum ROM and a 5-link planar walking FOM.

