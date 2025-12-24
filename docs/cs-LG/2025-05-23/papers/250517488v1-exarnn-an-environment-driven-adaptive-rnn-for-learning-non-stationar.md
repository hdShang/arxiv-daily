---
layout: default
title: ExARNN: An Environment-Driven Adaptive RNN for Learning Non-Stationary Power Dynamics
---

# ExARNN: An Environment-Driven Adaptive RNN for Learning Non-Stationary Power Dynamics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.17488" class="toolbar-btn" target="_blank">📄 arXiv: 2505.17488v1</a>
  <a href="https://arxiv.org/pdf/2505.17488.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.17488v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.17488v1', 'ExARNN: An Environment-Driven Adaptive RNN for Learning Non-Stationary Power Dynamics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoran Li, Muhao Guo, Yang Weng, Marija Ilic, Guangchun Ruan

**分类**: cs.LG, eess.SY

**发布日期**: 2025-05-23

**备注**: 5 pages, 3 figures, conference

---

## 💡 一句话要点

**提出ExARNN以解决非平稳电力动态建模问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `非平稳动态` `递归神经网络` `外部数据适应` `电力系统` `神经控制微分方程` `智能电网` `可再生能源`

## 📋 核心要点

1. 现有方法在捕捉非平稳电力动态时，无法有效整合外部环境因素，导致模型适应性不足。
2. 本文提出ExARNN，通过分层超网络设计，利用外部数据动态调整RNN参数，以实现更好的适应性。
3. 实验结果显示，ExARNN在电力动态预测中显著优于传统基线模型，验证了其有效性和优势。

## 📝 摘要（中文）

非平稳电力系统动态受到可再生能源波动、需求模式变化和气候变化的影响，变得愈加复杂。准确捕捉这些动态需要一个能够适应环境因素的模型。传统模型，包括递归神经网络（RNN），缺乏有效的机制来编码外部因素（如时间或环境数据）以实现动态适应。为此，本文提出了外部自适应RNN（ExARNN），这一新框架整合外部数据（如天气、时间）以持续调整基础RNN的参数。ExARNN通过分层超网络设计，利用神经控制微分方程（NCDE）处理外部数据并自适应生成RNN参数，从而能够处理电力与外部测量之间的不一致时间戳，确保持续适应。大量预测测试表明，ExARNN在性能上优于现有基线模型。

## 🔬 方法详解

**问题定义**：本文旨在解决非平稳电力系统动态建模中的适应性不足问题。现有的递归神经网络（RNN）无法有效处理外部环境因素的影响，导致预测性能下降。

**核心思路**：ExARNN的核心思想是通过整合外部数据（如天气和时间信息）来动态调整RNN的参数，从而提高模型的适应性和准确性。这种设计使得模型能够实时响应环境变化。

**技术框架**：ExARNN的整体架构包括一个基础RNN和一个分层超网络。超网络负责处理外部数据，并生成适应性的RNN参数。通过神经控制微分方程（NCDE），该框架能够有效处理时间戳不一致的问题。

**关键创新**：ExARNN的主要创新在于其分层超网络设计和使用NCDE处理外部数据的能力。这使得模型能够在动态环境中持续适应，而传统RNN则无法实现这一点。

**关键设计**：在参数设置上，ExARNN采用了特定的损失函数以优化预测性能，并在网络结构中引入了超网络模块，以确保外部数据的有效整合和参数生成。

## 📊 实验亮点

实验结果表明，ExARNN在电力动态预测中相较于传统基线模型提升了预测准确性，具体性能数据展示了在多个测试场景下，ExARNN的预测误差显著低于现有方法，验证了其优越性。

## 🎯 应用场景

ExARNN具有广泛的应用潜力，尤其在电力系统管理、可再生能源集成和智能电网等领域。其能够实时适应环境变化的特性，使其在动态电力市场和需求响应管理中具有重要的实际价值，未来可能推动电力系统的智能化发展。

## 📄 摘要（原文）

> Non-stationary power system dynamics, influenced by renewable energy variability, evolving demand patterns, and climate change, are becoming increasingly complex. Accurately capturing these dynamics requires a model capable of adapting to environmental factors. Traditional models, including Recurrent Neural Networks (RNNs), lack efficient mechanisms to encode external factors, such as time or environmental data, for dynamic adaptation. To address this, we propose the External Adaptive RNN (ExARNN), a novel framework that integrates external data (e.g., weather, time) to continuously adjust the parameters of a base RNN. ExARNN achieves this through a hierarchical hypernetwork design, using Neural Controlled Differential Equations (NCDE) to process external data and generate RNN parameters adaptively. This approach enables ExARNN to handle inconsistent timestamps between power and external measurements, ensuring continuous adaptation. Extensive forecasting tests demonstrate ExARNN's superiority over established baseline models.

