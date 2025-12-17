---
layout: default
title: In-Context Learning for Seismic Data Processing
---

# In-Context Learning for Seismic Data Processing

**arXiv**: [2512.11575v1](https://arxiv.org/abs/2512.11575) | [PDF](https://arxiv.org/pdf/2512.11575.pdf)

**作者**: Fabian Fuchs, Mario Ruben Fernandez, Norman Ettrich, Janis Keuper

---

## 💡 一句话要点

**提出ContextSeisNet，通过上下文学习解决地震数据去多次波中的空间不一致和用户控制不足问题。**

**关键词**: `地震数据处理` `上下文学习` `去多次波` `空间一致性` `数据效率`

## 📋 核心要点

1. 核心问题：传统和深度学习地震处理方法存在空间结果不一致和缺乏用户控制。
2. 方法要点：引入上下文学习模型，基于空间相关示例对进行预测，无需重新训练。
3. 实验或效果：在合成和现场数据上优于基线，提升空间一致性和数据效率。

## 📄 摘要（原文）

> Seismic processing transforms raw data into subsurface images essential for geophysical applications. Traditional methods face challenges, such as noisy data, and manual parameter tuning, among others. Recently deep learning approaches have proposed alternative solutions to some of these problems. However, important challenges of existing deep learning approaches are spatially inconsistent results across neighboring seismic gathers and lack of user-control. We address these limitations by introducing ContextSeisNet, an in-context learning model, to seismic demultiple processing. Our approach conditions predictions on a support set of spatially related example pairs: neighboring common-depth point gathers from the same seismic line and their corresponding labels. This allows the model to learn task-specific processing behavior at inference time by observing how similar gathers should be processed, without any retraining. This method provides both flexibility through user-defined examples and improved lateral consistency across seismic lines. On synthetic data, ContextSeisNet outperforms a U-Net baseline quantitatively and demonstrates enhanced spatial coherence between neighboring gathers. On field data, our model achieves superior lateral consistency compared to both traditional Radon demultiple and the U-Net baseline. Relative to the U-Net, ContextSeisNet also delivers improved near-offset performance and more complete multiple removal. Notably, ContextSeisNet achieves comparable field data performance despite being trained on 90% less data, demonstrating substantial data efficiency. These results establish ContextSeisNet as a practical approach for spatially consistent seismic demultiple with potential applicability to other seismic processing tasks.

