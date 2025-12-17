---
layout: default
title: LEC: Linear Expectation Constraints for False-Discovery Control in Selective Prediction and Routing Systems
---

# LEC: Linear Expectation Constraints for False-Discovery Control in Selective Prediction and Routing Systems

**arXiv**: [2512.01556v1](https://arxiv.org/abs/2512.01556) | [PDF](https://arxiv.org/pdf/2512.01556.pdf)

**作者**: Zhiyuan Wang, Aniri, Tianlong Chen, Yue Zhang, Heng Tao Shen, Xiaoshuang Shi, Kaidi Xu

---

## 💡 一句话要点

**提出LEC方法，通过线性期望约束实现选择性预测与路由系统中的错误发现率控制**

**关键词**: `错误发现率控制` `选择性预测` `线性期望约束` `模型路由` `大语言模型` `问答系统`

## 📋 核心要点

1. 核心问题：大语言模型生成不可靠答案，现有不确定性方法缺乏统计保证，导致用户接受错误预测
2. 方法要点：将选择性预测重构为带线性期望约束的决策问题，基于校准样本计算FDR约束下的覆盖最大化阈值
3. 实验或效果：在问答数据集上验证，LEC实现更严格的FDR控制，提高样本保留率，两模型路由机制降低风险并接受更多正确样本

## 📄 摘要（原文）

> Large language models (LLMs) often generate unreliable answers, while heuristic uncertainty methods fail to fully distinguish correct from incorrect predictions, causing users to accept erroneous answers without statistical guarantees. We address this issue through the lens of false discovery rate (FDR) control, ensuring that among all accepted predictions, the proportion of errors does not exceed a target risk level. To achieve this in a principled way, we propose LEC, which reinterprets selective prediction as a constrained decision problem by enforcing a Linear Expectation Constraint over selection and error indicators. Then, we establish a finite-sample sufficient condition, which relies only on a held-out set of exchangeable calibration samples, to compute an FDR-constrained, coverage-maximizing threshold. Furthermore, we extend LEC to a two-model routing mechanism: given a prompt, if the current model's uncertainty exceeds its calibrated threshold, we delegate it to a stronger model, while maintaining a unified FDR guarantee. Evaluations on closed-ended and open-ended question-answering (QA) datasets show that LEC achieves tighter FDR control and substantially improves sample retention over prior methods. Moreover, the two-model routing mechanism achieves lower risk levels while accepting more correct samples than each individual model.

