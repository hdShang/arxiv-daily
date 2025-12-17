---
layout: default
title: Black-Box Auditing of Quantum Model: Lifted Differential Privacy with Quantum Canaries
---

# Black-Box Auditing of Quantum Model: Lifted Differential Privacy with Quantum Canaries

**arXiv**: [2512.14388v1](https://arxiv.org/abs/2512.14388) | [PDF](https://arxiv.org/pdf/2512.14388.pdf)

**作者**: Baobao Song, Shiva Raj Pokhrel, Athanasios V. Vasilakos, Tianqing Zhu, Gang Li

**分类**: cs.LG

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于提升量子差分隐私的黑盒审计框架，利用量子金丝雀检测量子机器学习模型中的隐私泄露问题。**

**关键词**: `量子机器学习` `隐私审计` `差分隐私` `量子金丝雀` `黑盒验证` `隐私泄露检测` `量子计算安全` `模型记忆`

## 📋 核心要点

1. 现有量子差分隐私机制缺乏实证验证工具，无法评估已部署量子机器学习模型的隐私泄露风险。
2. 提出基于提升量子差分隐私的黑盒审计框架，利用量子金丝雀策略性编码量子态来检测记忆和量化隐私泄露。
3. 实验在模拟和物理硬件上验证了框架有效性，能精确测量隐私损失并建立理论到实践的桥梁。

## 📝 摘要（中文）

量子机器学习（QML）虽然具有显著的计算优势，但模型在敏感数据上训练时可能记忆个体记录，导致严重的隐私漏洞。现有的量子差分隐私（QDP）机制提供了理论上的最坏情况保证，但缺乏对已部署模型进行实证验证的工具。本文首次引入了基于提升量子差分隐私的黑盒隐私审计框架，利用量子金丝雀（策略性偏移编码的量子态）来检测记忆行为，并精确量化训练过程中的隐私泄露。该框架建立了金丝雀偏移与迹距离界限之间的严格数学联系，推导出隐私预算消耗的经验下界，从而弥合了理论保证与实际隐私验证之间的关键差距。在模拟和物理量子硬件上的全面评估表明，该框架能有效测量QML模型中的实际隐私损失，为QML系统提供稳健的隐私验证。

## 🔬 方法详解

论文提出一个黑盒隐私审计框架，核心基于提升量子差分隐私理论。整体框架通过引入量子金丝雀——即策略性偏移编码的量子态，作为探测工具来检测模型训练过程中的记忆行为。关键技术创新点在于建立了金丝雀偏移与量子态迹距离之间的严格数学联系，从而推导出隐私预算消耗的经验下界，这允许在无需访问模型内部细节的情况下量化隐私泄露。与现有方法的主要区别在于，现有量子差分隐私方法仅提供理论保证，而本框架首次实现了对QML模型的实证隐私验证，弥补了理论分析与实际部署之间的差距。

## 📊 实验亮点

在模拟和物理量子硬件上的实验表明，框架能有效检测模型记忆行为，精确量化隐私泄露，经验下界与理论保证一致，验证了提升量子差分隐私在实际系统中的适用性。

## 🎯 应用场景

该研究可应用于量子机器学习系统的隐私安全评估，特别是在医疗、金融等敏感数据处理场景中，帮助验证量子模型是否遵守隐私保护标准，促进QML技术的可信部署。

## 📄 摘要（原文）

> Quantum machine learning (QML) promises significant computational advantages, yet models trained on sensitive data risk memorizing individual records, creating serious privacy vulnerabilities. While Quantum Differential Privacy (QDP) mechanisms provide theoretical worst-case guarantees, they critically lack empirical verification tools for deployed models. We introduce the first black-box privacy auditing framework for QML based on Lifted Quantum Differential Privacy, leveraging quantum canaries (strategically offset-encoded quantum states) to detect memorization and precisely quantify privacy leakage during training. Our framework establishes a rigorous mathematical connection between canary offset and trace distance bounds, deriving empirical lower bounds on privacy budget consumption that bridge the critical gap between theoretical guarantees and practical privacy verification. Comprehensive evaluations across both simulated and physical quantum hardware demonstrate our framework's effectiveness in measuring actual privacy loss in QML models, enabling robust privacy verification in QML systems.

