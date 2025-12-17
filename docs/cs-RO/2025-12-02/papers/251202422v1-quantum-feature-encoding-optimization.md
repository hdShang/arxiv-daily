---
layout: default
title: Quantum feature encoding optimization
---

# Quantum feature encoding optimization

**arXiv**: [2512.02422v1](https://arxiv.org/abs/2512.02422) | [PDF](https://arxiv.org/pdf/2512.02422.pdf)

**作者**: Tommaso Fioravanti, Brian Quanz, Gabriele Agliardi, Edgar Andres Ruiz Guzman, Ginés Carrascal, Jae-Eun Park

---

## 💡 一句话要点

**提出量子特征编码优化方法，通过经典数据预处理提升量子机器学习模型性能**

**关键词**: `量子机器学习` `特征编码优化` `数据预处理` `量子电路` `模型性能提升` `硬件实验`

## 📋 核心要点

1. 核心问题：量子机器学习中数据编码对模型性能有决定性影响，但编码方式优化常被忽视
2. 方法要点：调整数据输入方式，如排序、选择和加权特征，作为编码前的预处理步骤
3. 实验或效果：在多种数据集和电路规模上验证，优化编码能显著且一致地提升模型性能，并在真实量子硬件上实现

## 📄 摘要（原文）

> Quantum Machine Learning (QML) holds the promise of enhancing machine learning modeling in terms of both complexity and accuracy. A key challenge in this domain is the encoding of input data, which plays a pivotal role in determining the performance of QML models. In this work, we tackle a largely unaddressed aspect of encoding that is unique to QML modeling -- rather than adjusting the ansatz used for encoding, we consider adjusting how data is conveyed to the ansatz. We specifically implement QML pipelines that leverage classical data manipulation (i.e., ordering, selecting, and weighting features) as a preprocessing step, and evaluate if these aspects of encoding can have a significant impact on QML model performance, and if they can be effectively optimized to improve performance. Our experimental results, applied across a wide variety of data sets, ansatz, and circuit sizes, with a representative QML approach, demonstrate that by optimizing how features are encoded in an ansatz we can substantially and consistently improve the performance of QML models, making a compelling case for integrating these techniques in future QML applications. Finally we demonstrate the practical feasibility of this approach by running it using real quantum hardware with 100 qubit circuits and successfully achieving improved QML modeling performance in this case as well.

