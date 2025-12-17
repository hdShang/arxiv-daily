---
layout: default
title: Inverse Optimal Control of Muscle Force Sharing During Pathological Gait
---

# Inverse Optimal Control of Muscle Force Sharing During Pathological Gait

**arXiv**: [2510.17456v1](https://arxiv.org/abs/2510.17456) | [PDF](https://arxiv.org/pdf/2510.17456.pdf)

**作者**: Filip Bečanović, Vincent Bonnet, Kosta Jovanović, Samer Mohammed, Raphaël Dumas

---

## 💡 一句话要点

**应用逆最优控制识别中风后步态中肌肉力分配的最佳目标函数**

**关键词**: `逆最优控制` `肌肉力分配` `病理步态` `中风康复` `目标函数优化`

## 📋 核心要点

1. 核心问题：如何确定中风后步态中肌肉力分配的最佳目标函数，以近似神经控制策略。
2. 方法要点：使用逆最优控制，从基础目标函数的正线性组合中识别个体和腿部特定的最佳函数。
3. 实验效果：模型在各自肢体上表现良好，但跨对象泛化差，尤其对偏瘫腿。

## 📄 摘要（原文）

> Muscle force sharing is typically resolved by minimizing a specific objective
> function to approximate neural control strategies. An inverse optimal control
> approach was applied to identify the "best" objective function, among a
> positive linear combination of basis objective functions, associated with the
> gait of two post-stroke males, one high-functioning (subject S1) and one
> low-functioning (subject S2). It was found that the "best" objective function
> is subject- and leg-specific. No single function works universally well, yet
> the best options are usually differently weighted combinations of muscle
> activation- and power-minimization. Subject-specific inverse optimal control
> models performed best on their respective limbs (\textbf{RMSE 178/213 N, CC
> 0.71/0.61} for non-paretic and paretic legs of S1; \textbf{RMSE 205/165 N, CC
> 0.88/0.85} for respective legs of S2), but cross-subject generalization was
> poor, particularly for paretic legs. Moreover, minimizing the root mean square
> of muscle power emerged as important for paretic limbs, while minimizing
> activation-based functions dominated for non-paretic limbs. This may suggest
> different neural control strategies between affected and unaffected sides,
> possibly altered by the presence of spasticity. Among the 15 considered
> objective functions commonly used in inverse dynamics-based computations, the
> root mean square of muscle power was the only one explicitly incorporating
> muscle velocity, leading to a possible model for spasticity in the paretic
> limbs. Although this objective function has been rarely used, it may be
> relevant for modeling pathological gait, such as post-stroke gait.

